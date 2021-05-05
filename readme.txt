1. install geopandas ใน andconda
    conda install -c conda-forge geopandas
2. unzip ข้อมูล shp ลงใน directory 
3. สร้าง direcectory ชื่อ json
4. เรียกใช้ python toGeoJson.py จะทำการอ่านแต่ละ directory แล้วสร้างแฟ้ม geojoson ลงใน direcotry json 
5. ทำการแก้ toRecord.ini เพื่อกำหนด layer ที่จะทำการแปลง geoJson เป็น record ที่จะนำเข้า database จะมีการสร้างข้อมูลลงใน json/record directory
6. เรียก python toRecord.py
7. เรัยก python toDatabase.py จะทำการ upload ข้อมูลขึ้นไปยังฐานข้อมูล

ืหมายเหตุ
=======
แฟ้มใน directory จะต้องชือ่เดียวกับ directory  เช่น directory ชื่อ airport จะมีแฟ้มชื่อ airport หมด 