# ServerlessAws
# My First Serverless Function+ (Ödev Projesi)

Bu proje, bulutta sunucusuz (serverless) çalışan bir API geliştirme ödevidir.
AWS Lambda ve API Gateway kullanılarak geliştirilmiştir.

##  Fonksiyonun Yaptığı İş

Geliştirilen fonksiyon, bir HTTP GET isteği ile tetiklenir.
İsteğe bağlı olarak bir `name` parametresi alır ve kişiselleştirilmiş bir JSON mesajı döndürür.

* **Endpoint URL:** `[Buraya Adım 3'teki API Gateway URL'ini yapıştır]`

## Nasıl Deploy Edilir?

Bu fonksiyon AWS Konsolu üzerinden manuel olarak deploy edilmiştir:
1.  **AWS Lambda:** `Python 3.10` runtime seçilerek `hello-api-function` adında bir fonksiyon oluşturuldu.
2.  **IAM Rolü:** Fonksiyon için otomatik olarak `AWSLambdaBasicExecutionRole` yetkisine sahip bir IAM rolü oluşturuldu. Bu rol, fonksiyonun sadece CloudWatch'a log yazabilmesi için "en az yetki prensibine" uygundur.
3.  **Kod:** `lambda_function.py` dosyasındaki kod, Lambda konsolundaki kod editörüne yapıştırıldı ve "Deploy" edildi.
4.  **Tetikleyici:** Fonksiyona "API Gateway" tetikleyicisi eklendi. "HTTP API" tipi ve "Open" güvenlik ayarı seçilerek internetten erişilebilir bir API endpoint'i oluşturuldu.

##  Test Senaryosu (Örnek Input/Output)

API'yi test etmek için bir tarayıcı veya `curl` kullanılabilir.

### Senaryo 1: Parametresiz İstek

**Input (İstek):**
```bash
curl "https://[SENIN-API-URL]/hello-api-function/"
{<img width="1919" height="839" alt="Ekran görüntüsü 2025-10-22 203953" src="https://github.com/user-attachments/assets/5de5ad25-b532-4da0-ab6d-368c9c29d43f" />

  "message": "Merhaba dostum, bu fonksiyon bulutta çalışıyor!",
  "input_event": { ... }<img width="1551" height="875" alt="Ekran görüntüsü 2025-10-22 203913" src="https://github.com/user-attachments/assets/6d0aad82-f238-4cea-b67e-6a43fcf97b98" />

}
