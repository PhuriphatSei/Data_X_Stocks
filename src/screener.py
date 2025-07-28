import yfinance as yf
import pandas as pd
import os
from valuation_dcf import dcf_valuation
from valuation_graham import graham_valuation
from pe_roe_trend import plot_pe_roe_trend

# ตัวหลัก 10 ตัว (ที่อยากดึงข้อมูลก่อน)
set50_symbols = [
    "AOT.BK", "PTT.BK", "CPALL.BK", "ADVANC.BK", "INTUCH.BK", "KBANK.BK",
    "BDMS.BK", "BBL.BK", "GULF.BK", "PTTEP.BK"
]

# รายชื่อหุ้น SET50 ทั้งหมด (ตัวอย่าง) — เปลี่ยนเป็นรายชื่อจริง SET50 ที่คุณมี
full_set50_symbols = [
    "AOT.BK", "PTT.BK", "CPALL.BK", "ADVANC.BK", "INTUCH.BK", "KBANK.BK", "BDMS.BK",
    "BBL.BK", "GULF.BK", "PTTEP.BK", "GPSC.BK", "TOP.BK", "TRUE.BK", "BAM.BK", "MINT.BK",
    "BTS.BK", "HMPRO.BK", "IVL.BK", "OR.BK", "PTTGC.BK", "SCB.BK", "SCC.BK", "TISCO.BK",
    "TMB.BK", "BH.BK", "CPN.BK", "DTAC.BK", "ESSO.BK", "GLOBAL.BK", "GUNKUL.BK", "IRPC.BK",
    "KCE.BK", "KTB.BK", "LH.BK", "LPN.BK", "MBK.BK", "MC.BK", "MEGA.BK", "MTC.BK", "OSP.BK",
    "PLANB.BK", "PRM.BK", "PTG.BK", "QH.BK", "RATCH.BK", "ROBINS.BK", "SCGP.BK", "SIRI.BK",
    "SPALI.BK", "STA.BK", "STGT.BK", "TASCO.BK"
]

def filter_valid_symbols(symbols, full_list):
    valid = []
    invalid = []

    for symbol in symbols:
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            if all(info.get(k) is not None for k in [
                'currentPrice', 'trailingPE', 'priceToBook', 'returnOnEquity',
                'sharesOutstanding', 'trailingEps', 'bookValue'
            ]):
                if not stock.financials.empty and 'Net Income' in stock.financials.index:
                    valid.append(symbol)
                else:
                    print(f"⚠️ ไม่มี Net Income สำหรับ {symbol}, ข้าม")
                    invalid.append(symbol)
            else:
                print(f"⚠️ ข้อมูลไม่ครบสำหรับ {symbol}, ข้าม")
                invalid.append(symbol)
        except Exception as e:
            print(f"❌ Error ตรวจสอบ {symbol}: {e}")
            invalid.append(symbol)

    used = set(valid + symbols)
    # ไล่แทนที่ตัวไม่ผ่านด้วยตัวที่ยังไม่ใช้ใน full_set50_symbols
    for _ in range(len(invalid)):
        candidate = None
        for s in full_list:
            if s not in used:
                candidate = s
                break
        if candidate is None:
            print("⚠️ หมดตัวสำรองแล้ว ไม่สามารถแทนที่ได้อีก")
            break

        try:
            stock = yf.Ticker(candidate)
            info = stock.info
            if all(info.get(k) is not None for k in [
                'currentPrice', 'trailingPE', 'priceToBook', 'returnOnEquity',
                'sharesOutstanding', 'trailingEps', 'bookValue'
            ]):
                if not stock.financials.empty and 'Net Income' in stock.financials.index:
                    print(f"✅ แทนที่ด้วย {candidate}")
                    valid.append(candidate)
                    used.add(candidate)
                else:
                    print(f"⚠️ ไม่มี Net Income สำหรับ {candidate}, ข้าม")
            else:
                print(f"⚠️ ข้อมูลไม่ครบสำหรับ {candidate}, ข้าม")
        except Exception as e:
            print(f"❌ Error ตรวจสอบ {candidate}: {e}")

    return valid

# ฟังก์ชันอื่นๆ เหมือนเดิม
def fetch_stock_data(symbols):
    results = []
    for symbol in symbols:
        try:
            stock = yf.Ticker(symbol)
            info = stock.info

            price = info.get('currentPrice') or info.get('regularMarketPrice')
            pe = info.get('trailingPE')
            pb = info.get('priceToBook')
            roe = info.get('returnOnEquity')
            shares = info.get('sharesOutstanding')
            eps = info.get('trailingEps')
            book_value_per_share = info.get('bookValue')

            try:
                net_income = stock.financials.loc['Net Income'].iloc[0]
            except:
                net_income = None

            if None in (price, pe, pb, roe, shares, eps, book_value_per_share, net_income):
                print(f"⚠️ ข้อมูลไม่ครบสำหรับ {symbol}, ข้าม")
                continue

            dcf = dcf_valuation(
                fcff_now=net_income,
                growth_rate=0.08,
                wacc=0.085,
                shares_outstanding=shares
            )

            graham_val = graham_valuation(eps, book_value_per_share)

            results.append({
                'Symbol': symbol,
                'Price': round(price, 4),
                'PE': round(pe, 4),
                'PBV': round(pb, 4),
                'ROE': round(roe, 4),
                'EPS': round(eps, 4),
                'BVPS': round(book_value_per_share, 4),
                'DCF Price': round(dcf['intrinsic_value_per_share'], 4),
                'Graham Price': round(graham_val, 4) if graham_val else None,
                'Undervalue DCF %': round(((dcf['intrinsic_value_per_share'] - price) / price) * 100, 4),
                'Undervalue Graham %': round(((graham_val - price) / price) * 100, 4) if graham_val else None,
            })

        except Exception as e:
            print(f"❌ Error สำหรับ {symbol}: {e}")

    return pd.DataFrame(results)

if __name__ == "__main__":
    os.makedirs("data/raw", exist_ok=True)

    print("🔍 ตรวจสอบ symbol ที่ใช้ได้...")
    valid_symbols = filter_valid_symbols(set50_symbols, full_set50_symbols)
    print(f"✅ หุ้นที่ข้อมูลครบ: {valid_symbols}")

    df = fetch_stock_data(valid_symbols)
    df.to_csv("data/raw/set50_top_10_stock_data.csv", index=False)
    print("✅ บันทึกข้อมูลเสร็จที่ data/raw/set50_top_10_stock_data.csv")
    print("📊 กำลังวาดกราฟ PE vs ROE...")
    plot_pe_roe_trend(df)
