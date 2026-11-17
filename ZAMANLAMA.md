# Zamanlama seçenekleri

Kaynak: Claude Code resmî belgeleri (code.claude.com/docs), 17 Kas 2026'da okundu. Hiçbiri bu projede KURULU DEĞİL; kurmak Selma'nın kararı.

| Yol | Nerede çalışır | Yerel dosya | claude.ai bağlayıcıları (Higgsfield) | Sınır |
|---|---|---|---|---|
| Bulut zamanlanmış görev (`/schedule`, eski adı routine) | Anthropic bulutu, repo her koşuda sıfırdan klonlanır | Yok | Var, varsayılan olarak hepsi dahil | En sık saatte bir; araştırma önizlemesi; claude.ai aboneliği ister |
| Masaüstü zamanlanmış görev | Senin Mac'in | Var | Var (oturum açıksa) | Uygulama açık ve Mac uyanık olmalı; en sık saatte bir |
| `/loop` | Açık oturumun içi | Var | Var | Terminal kapanınca durur; en sık dakikada bir; 7 günde biter |
| Başsız mod (`claude -p "/siradaki-bolum"`) | Komutu çalıştıran makine | Var | Oturum açıksa belgeler "otomatik kullanılabilir" diyor; `-p` için açıkça doğrulanmıyor | cron/launchd ile çalıştırmak belgelenmiş bir kalıp değil |
| GitHub Actions (`anthropics/claude-code-action`) | GitHub | Repo | Belgede yok | Zamanlama herkese açık repoda 60 gün hareketsizlikte kapanır |

## Bu proje için sonuçlar
- **Bulut görevi** Higgsfield bağlayıcısını kullanabilir ama yerel klasörü göremez. Projenin bir GitHub reposunda olması ve çıktının repoya ya da Higgsfield hesabına yazılması gerekir.
- **Kendi bilgisayarında** en az sürtünmeli yol masaüstü zamanlanmış görevdir: yerel dosyalar ve bağlayıcı ikisi de var; bedeli, bilgisayarın açık kalması.
- **Sunucu (VPS) + abonelik:** `claude setup-token` bir yıllık jeton üretir ve "CI, betik ve tarayıcıyla girişin olmadığı ortamlar" için belgelenmiştir. Ama bu jeton claude.ai bağlayıcılarını ÇEKEMEZ; yani sunucuda Higgsfield bağlayıcısı gelmez, MCP'nin ayrıca kurulması ve etkileşimli bir oturumda bir kez yetkilendirilmesi gerekir.
- **Şartlar:** abonelik girişi "olağan, bireysel kullanım" içindir; başkalarına hizmet veren ürünler API anahtarı kullanmalıdır. Kişisel, sürekli açık bir sunucunun buna girip girmediği belgelerde açıkça yazmıyor (doğrulanmadı).

## Komut
Sıradaki bölümü elle çalıştırmak: proje klasöründe Claude Code'u aç, `/siradaki-bolum` yaz.
Başsız çalıştırmak: `claude -p "/siradaki-bolum"` (izin gereken adımlar için `--permission-mode` ayarı gerekir).
