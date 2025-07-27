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

<img width="1103" height="449" alt="image" src="https://github.com/user-attachments/assets/2da09a68-97f8-4910-acbb-45c9299f56f7" />


------------------------------------------------------------------------------------------------------------------------------
