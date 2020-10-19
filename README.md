# login-twitter-and-post

Script ini di gunakan untuk automated test dengan Python - Selenium login test, post tweet, and post image di twitter.

## Persiapan + Instalasi

    - Pastikan python dan selenium sudah terinstall di PC kalian.
    - Pastikan Git sudah terinstall di PC kalian. (tidak wajib).
    - kalau belum terinstall, silahkan lihat di https://www.seleniummaster.com/sitecontent/index.php/selenium-web-driver-menu/selenium-test-automation-with-python/186-how-to-install-selenium-python-webdriver untuk cara instalasi python-selenium.
    - Pastikan kalian mempunyai chromeDriver di PC kalian.

### Getting the code

Kode ini hosted di https://github.com/endrat12/login-twitter-and-post.git
Silahkan follow intruksi dibawah::

1. Pastikan python unittest terinstall di PC kalian, kalau belum silahkan ketik "python -m unittest" di cmd kalian dan tunggu sampai installasi selesai.
2. Open CMD or Git Bush dan input command:

        cd Desktop (*untuk "Desktop" Kalian bisa mengganti dengan directory/drive yang kalian mau*)
  
        git clone https://github.com/endrat12/login-twitter-and-post.git
  
Tunggu sampai clone selesai. Dan setelah selesai, silahkan check di Desktop kalian, maka akan ada folder baru yang berisi project ini.

Contoh command di atas yang saya gunakan di PC:

    cd Desktop
  
    git clone https://github.com/endrat12/login-twitter-and-post.git
  

### Running the Test.

1. Silahkan buka CMD atau git bush kalian.
2. Silahkan ketik:

        cd (directory dimana kalian menyimpan folder clone tadi) terus tekan enter
  
   contoh: cd C:\Users\remote\Desktop\login-twitter-and-post
  
3. Silahkan ketik:

        python twitter.login.py terus tekan enter
    
4. Silahkan ikuti interuksi yang akan muncul di CMD atau git bush kalian setelah run script seperti diatas, seperti dibawah ini:

        Enter your name or email : "silahkan isi dengan nama ato email akun twitter kalian" terus tekan enter
  
        Enter your password : "Silahkan isi dengan password akun twitter kalian" terus tekan enter
  
        Enter your image path : "Silahkan isi directory dimana foto atau gambar kalian yang kalian mau post berada, contoh "C:\Users\remote\Desktop\angel.jpg"" terus tekan enter
  
        Enter your tweet : "Isi dengan kata ato kalimat yang kalian ingin post" terus tekan enter
  
5. Silahkan tunggu sampai proses script diatas selesai.

NOTE : Apabila Chrome browser tiba-tiba closed saat proses script running, silahkan ulangi dari step ke 4.


## Built With

* [PyCharm 2020.1.3 x64]
