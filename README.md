# Data_X_Stocks

**Description**
This project fetches fundamental financial data for selected SET50 stocks using the yfinance library. It collects key metrics such as Price, PE ratio, PBV, ROE, EPS, Book Value per Share, and Net Income. Using these data points, it calculates intrinsic stock valuations based on Discounted Cash Flow (DCF) and Graham Number methods.
The project includes functionality to:

- Validate stock symbols and automatically replace any invalid or incomplete data symbols with backup symbols from a full SET50 list.
- Fetch and process financial data, ensuring completeness and availability of necessary financial items.
- Calculate intrinsic stock values based on provided growth, WACC, and shares outstanding.
- Generate a PE vs ROE scatter plot visualizing the valuation data, saved as a PNG image.

This tool is useful for fundamental stock analysis, valuation comparison, and visual data exploration of SET50 stocks.

------------------------------------------------------------------------------------------------------------------------------
**คำอธิบาย**

โปรเจกต์นี้ดึงข้อมูลการเงินพื้นฐานของหุ้นในกลุ่ม SET50 โดยใช้ไลบรารี yfinance โดยเก็บข้อมูลสำคัญ เช่น ราคา, อัตราส่วน PE, PBV, ROE, EPS, มูลค่าตามบัญชีต่อหุ้น และกำไรสุทธิ

โปรเจกต์นี้มีฟังก์ชันสำหรับ:

- ตรวจสอบ symbol หุ้นที่ใช้ได้ และแทนที่ symbol ที่ไม่สมบูรณ์หรือใช้งานไม่ได้ด้วย symbol สำรองจากรายชื่อหุ้น SET50 ทั้งหมด
- ดึงและประมวลผลข้อมูลการเงิน โดยตรวจสอบความครบถ้วนของข้อมูลที่จำเป็น
- คำนวณมูลค่าพื้นฐานของหุ้นโดยใช้วิธี Discounted Cash Flow (DCF) และ Graham Number โดยอิงจากอัตราการเติบโต, ต้นทุนทุนเฉลี่ยถ่วงน้ำหนัก (WACC), และจำนวนหุ้นจดทะเบียน
- สร้างกราฟกระจาย PE เทียบกับ ROE เพื่อแสดงภาพรวมการประเมินมูลค่าหุ้น พร้อมบันทึกเป็นไฟล์ PNG

เครื่องมือนี้เหมาะสำหรับนักวิเคราะห์หุ้นที่ต้องการวิเคราะห์มูลค่าพื้นฐาน เปรียบเทียบหุ้น และสำรวจข้อมูลด้วยภาพสำหรับหุ้น SET50

------------------------------------------------------------------------------------------------------------------------------

**📖 File Structure**

<img width="730" height="318" alt="image" src="https://github.com/user-attachments/assets/c9dbf080-a99b-491a-a99c-da5e2b42072f" />

------------------------------------------------------------------------------------------------------------------------------

**📊 Result**

<img width="3000" height="1800" alt="pe_roe_trend" src="https://github.com/user-attachments/assets/26b04472-e879-4346-a91d-f941ad9a0903" />



------------------------------------------------------------------------------------------------------------------------------
### 📘 คำอธิบายคำศัพท์

| คำศัพท์                           | ความหมาย                                           | สูตรหรือแนวคิด                                                                 |
|-----------------------------------|----------------------------------------------------|--------------------------------------------------------------------------------|
| **Symbol**                        | ชื่อย่อของหุ้น (เช่น AOT, PTT)                           | ใช้สำหรับอ้างอิงหุ้นแต่ละตัว                                                          |
| **Price**                         | ราคาหุ้นปัจจุบัน (บาท/หุ้น)                              | ราคาล่าสุดจากตลาด                                                                |
| **PE**<br>(Price/Earnings)        | อัตราส่วนราคาต่อกำไรสุทธิ                               | `Price / EPS`<br>ใช้วัดว่าหุ้นแพงหรือถูกเมื่อเทียบกับกำไร                                 |
| **PBV**<br>(Price/Book Value)     | อัตราส่วนราคาต่อมูลค่าทางบัญชี                           | `Price / BVPS`<br>ใช้เปรียบเทียบราคาหุ้นกับสินทรัพย์สุทธิ                                |
| **ROE**<br>(Return on Equity)     | ผลตอบแทนผู้ถือหุ้น (%)                                | `EPS / BVPS * 100`<br>บ่งบอกว่าบริษัททำกำไรได้ดีแค่ไหนจากทุนผู้ถือหุ้น                    |
| **EPS**<br>(Earnings Per Share)   | กำไรสุทธิต่อหุ้น                                        | `กำไรสุทธิ / จำนวนหุ้น`                                                           |
| **BVPS**<br>(Book Value Per Share) | มูลค่าทางบัญชีต่อหุ้น                                   | `ส่วนของผู้ถือหุ้น / จำนวนหุ้น`                                                      |
| **DCF Price**                      | ราคาหุ้นที่เหมาะสมตามการประเมินด้วย DCF                  | ประเมินจากกระแสเงินสดในอนาคตของบริษัท                                             |
| **Graham Price**                   | ราคาหุ้นตามสูตร Benjamin Graham                      | `√(22.5 × EPS × BVPS)`<br>เหมาะกับการวิเคราะห์หุ้นคุณค่า (Value Stock)                |
| **Undervalue DCF %**               | ส่วนต่างราคาจาก DCF (%)                              | `(DCF Price - Price) / Price * 100`<br>ค่าบวก = หุ้นต่ำกว่าราคาประเมิน (น่าซื้อ)       |
| **Undervalue Graham %**            | ส่วนต่างราคาจาก Graham (%)                           | `(Graham Price - Price) / Price * 100`<br>ค่าบวก = หุ้นต่ำกว่าราคาประเมินตาม Graham |


------------------------------------------------------------------------------------------------------------------------------

### 📊 ผลลัพท์พร้อมคำอธิบาย

---

#### 🛫 AOT.BK – ท่าอากาศยานไทย  
**Price:** 42.0 | **DCF:** 27.21 | **Graham:** 16.18  
- ROE ต่ำมาก (0.16%) → ผลตอบแทนผู้ถือหุ้นต่ำ  
- PE สูง (31.1) → แพงเทียบกับกำไร  
- ✅ หุ้น **Overvalued อย่างมาก** ทั้งตาม DCF และ Graham  

---

#### ⛽ PTT.BK – ปตท  
**Price:** 32.25 | **DCF:** 64.36 | **Graham:** 52.13  
- ROE ต่ำ (6.19%) แต่ EPS ดี (2.95)  
- ✅ Undervalue ทั้ง DCF (+99.6%) และ Graham (+61.6%) → **น่าสนใจในเชิง Value Investing**  
- 📉 PBV ต่ำ (0.78) → ราคาต่ำกว่าทุนบริษัท  

---

#### 🛍️ CPALL.BK – เซเว่น  
**Price:** 46.5 | **DCF:** 57.43 | **Graham:** 30.14  
- PE ปานกลาง (15.98), ROE ยังพอใช้  
- ✅ DCF บอกถูกเล็กน้อย (+23.5%)  
- ❌ Graham บอกแพง (-35.2%)  
- ❗ ควรวิเคราะห์เพิ่มเรื่องการเติบโต  

---

#### 📱 ADVANC.BK – AIS  
**Price:** 293.0 | **DCF:** 238.99 | **Graham:** 92.65  
- ROE สูง (42%) → ธุรกิจมีคุณภาพ  
- ❌ ราคาแพงจากทั้ง DCF และ Graham  
- แต่เป็น **หุ้นปันผลสูง – Defensive Stock**  

---

#### 🏦 KBANK.BK – ธนาคารกสิกร  
**Price:** 159.0 | **DCF:** 415.67 | **Graham:** 327.67  
- ✅ Undervalue มาก!!: DCF (+161%), Graham (+106%)  
- EPS สูง (20.27), ROE พอใช้  
- เหมาะสำหรับ **นักลงทุนระยะยาว/ปันผล**  

---

#### 🏥 BDMS.BK – กรุงเทพดุสิตเวชการ  
**Price:** 21.0 | **DCF:** 20.39 | **Graham:** 12.29  
- PE, PBV สูง → ราคาสูงเกินสินทรัพย์และกำไร  
- ❌ แทบไม่มี upside ทั้ง DCF และ Graham  
- หุ้นดี แต่ราคาน่าจะเต็มมูลค่า  

---

#### 🏦 BBL.BK – ธนาคารกรุงเทพ  
**Price:** 147.5 | **DCF:** 479.99 | **Graham:** 409.2  
- ✅ Undervalue มากที่สุดในกลุ่ม  
- ROE ต่ำ (8.5%) แต่ EPS สูง (24.79), PBV ต่ำ (0.49)  
- หุ้นธนาคารที่ **ดูปลอดภัยและราคาถูก**  

---

#### ⚡ GULF.BK – กัลฟ์  
**Price:** 46.5 | **DCF:** 24.65 | **Graham:** 19.49  
- ❌ Overvalued จากทั้งสองมุมมอง  
- PE สูง (27), ROE ค่อนข้างดี  
- อาจสะท้อน **การเก็งกำไร/คาดหวังสูง**  

---

#### 🛢️ PTTEP.BK – ปตท.สผ.  
**Price:** 116.0 | **DCF:** 402.37 | **Graham:** 38.98  
- ✅ DCF Undervalue มากถึง +246.8%  
- ❌ Graham ต่ำกว่า → อาจมี **EPS–BV ผิดปกติ**  
- หุ้นพลังงาน → ควรดูราคาน้ำมันประกอบ  

---

#### ⚡ GPSC.BK – พลังงานไฟฟ้า  
**Price:** 32.25 | **DCF:** 29.2 | **Graham:** 36.37  
- Graham Price สูงกว่า → **Graham undervalue**  
- PE สูง (21), ROE ต่ำ (4.18%)  
- ธุรกิจเติบโต แต่ต้องรอ **ผลตอบแทนในอนาคต**  

------------------------------------------------------------------------------------------------------------------------------
