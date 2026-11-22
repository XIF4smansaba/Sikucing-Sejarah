from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# =====================================================================
# 1. ARRAY (LIST): Bank Soal 4 Stage (6 PG + 2 Esai per Stage)
# =====================================================================
ARRAY_STAGE = [
    {
        "stage_id": 1,
        "judul": "Stage 1: Perang Aceh",
        "soal": [
            {
                "tipe": "pg",
                "pertanyaan": "Perjanjian tahun 1871 yang membiarkan Belanda memperluas kekuasaan di Sumatra termasuk Aceh adalah...",
                "opsi": ["Traktat Sumatra", "Traktat London", "Perjanjian Giyanti"],
                "benar": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Pemimpin Ekspedisi I Belanda (April 1873) yang tewas di depan Masjid Raya Baiturrahman adalah...",
                "opsi": ["Jenderal van Swieten", "Mayjen J.H.R. Köhler", "Jenderal Van Heutsz"],
                "benar": 1
            },
            {
                "tipe": "pg",
                "pertanyaan": "Tokoh Aceh yang berpura-pura menyerah pada 1893 untuk mendapat senjata lalu berbalik melawan (1896) adalah...",
                "opsi": ["Panglima Polim", "Teungku Chik di Tiro", "Teuku Umar"],
                "benar": 2
            },
            {
                "tipe": "pg",
                "pertanyaan": "Karya sastra yang dibacakan untuk membakar semangat jihad (perang sabil) rakyat Aceh adalah...",
                "opsi": ["Hikayat Perang Sabi", "De Atjehers", "Babad Tanah Jawi"],
                "benar": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Ahli Islam Belanda yang meneliti Aceh (1891–1892) dan merumuskan strategi penaklukan Aceh adalah...",
                "opsi": ["Jenderal De Kock", "Snouck Hurgronje", "C.Th. van Deventer"],
                "benar": 1
            },
            {
                "tipe": "pg",
                "pertanyaan": "Pasukan khusus keliling yang dibentuk Belanda untuk menumpas gerilya Aceh adalah...",
                "opsi": ["VOC", "Benteng Stelsel", "Marsose"],
                "benar": 2
            },
            {
                "tipe": "esai",
                "pertanyaan": "[ESAI 1] Apa nama 'Pernyataan Pendek' yang ditandatangani kaum uleebalang untuk mengakui kekuasaan Belanda?",
                "kata_kunci": ["korte verklaring", "pernyataan pendek"],
                "contoh_benar": "Korte Verklaring"
            },
            {
                "tipe": "esai",
                "pertanyaan": "[ESAI 2] Siapa istri Teuku Umar yang meneruskan perang gerilya di pedalaman hingga diasingkan ke Sumedang?",
                "kata_kunci": ["cut nyak dhien", "cut nyak dien"],
                "contoh_benar": "Cut Nyak Dhien"
            }
        ]
    },
    {
        "stage_id": 2,
        "judul": "Stage 2: Perlawanan Banten",
        "soal": [
            {
                "tipe": "pg",
                "pertanyaan": "Komoditas utama yang menjadikan Banten bandar dagang besar dan pesaing berat VOC pada abad ke-17 adalah...",
                "opsi": ["Lada", "Gula", "Cengkih"],
                "benar": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Putra Sultan Ageng Tirtayasa yang diangkat menjadi sultan muda namun kemudian bersekutu dengan VOC adalah...",
                "opsi": ["Pangeran Purbaya", "Sultan Haji", "Syekh Yusuf"],
                "benar": 1
            },
            {
                "tipe": "pg",
                "pertanyaan": "Ulama pendukung Sultan Ageng yang ditangkap VOC lalu diasingkan ke Sri Lanka dan Afrika Selatan adalah...",
                "opsi": ["Kyai Mojo", "Teungku Chik di Tiro", "Syekh Yusuf"],
                "benar": 2
            },
            {
                "tipe": "pg",
                "pertanyaan": "Nama istana Kesultanan Banten yang diambil alih oleh Sultan Haji pada tahun 1680 adalah...",
                "opsi": ["Surosowan", "Kartasura", "Tegalrejo"],
                "benar": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Politik adu domba yang diterapkan VOC untuk memecah belah ayah dan anak di Banten disebut...",
                "opsi": ["Cultuurstelsel", "Devide et Impera", "Konsentrasi Stelsel"],
                "benar": 1
            },
            {
                "tipe": "pg",
                "pertanyaan": "Wilayah yang harus diserahkan Banten kepada VOC melalui perjanjian tahun 1684 adalah...",
                "opsi": ["Surakarta", "Meulaboh", "Lampung"],
                "benar": 2
            },
            {
                "tipe": "esai",
                "pertanyaan": "[ESAI 1] Siapa nama Sultan Banten (1651–1683) yang menerapkan perdagangan bebas dan gigih melawan VOC?",
                "kata_kunci": ["sultan ageng tirtayasa", "ageng tirtayasa"],
                "contoh_benar": "Sultan Ageng Tirtayasa"
            },
            {
                "tipe": "esai",
                "pertanyaan": "[ESAI 2] Siapa nama asli Sultan Haji sebelum bergelar sultan muda?",
                "kata_kunci": ["abdul kahar"],
                "contoh_benar": "Abdul Kahar"
            }
        ]
    },
    {
        "stage_id": 3,
        "judul": "Stage 3: Geger Pacinan & Diponegoro",
        "soal": [
            {
                "tipe": "pg",
                "pertanyaan": "Peristiwa pembantaian penduduk Tionghoa di Batavia pada Oktober 1740 juga dikenal sebagai...",
                "opsi": ["Tragedi Angke", "Peristiwa Garut", "Perang Sabil"],
                "benar": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Gubernur Jenderal VOC yang memimpin pembantaian etnis Tionghoa di Batavia pada 1740 adalah...",
                "opsi": ["Van den Bosch", "Adriaan Valckenier", "Jenderal De Kock"],
                "benar": 1
            },
            {
                "tipe": "pg",
                "pertanyaan": "Tokoh yang dinobatkan pasukan gabungan Tionghoa-Jawa di Kartasura bergelar Sunan Kuning adalah...",
                "opsi": ["Pakubuwono II", "Cakraningrat IV", "Raden Mas Garendi"],
                "benar": 2
            },
            {
                "tipe": "pg",
                "pertanyaan": "Sebab khusus Perang Diponegoro (1825) adalah pemasangan patok jalan melintasi makam leluhur di...",
                "opsi": ["Tegalrejo", "Selarong", "Magelang"],
                "benar": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Strategi pos benteng yang dihubungkan jalan oleh Jenderal De Kock untuk mempersempit gerak Diponegoro disebut...",
                "opsi": ["Konsentrasi Stelsel", "Benteng Stelsel", "Politik Etis"],
                "benar": 1
            },
            {
                "tipe": "pg",
                "pertanyaan": "Kota tempat Pangeran Diponegoro ditangkap saat perundingan pada 28 Maret 1830 adalah...",
                "opsi": ["Yogyakarta", "Ponorogo", "Magelang"],
                "benar": 2
            },
            {
                "tipe": "esai",
                "pertanyaan": "[ESAI 1] Siapa penasihat spiritual Pangeran Diponegoro yang turut mendukung perlawanan?",
                "kata_kunci": ["kyai mojo", "kiai mojo"],
                "contoh_benar": "Kyai Mojo"
            },
            {
                "tipe": "esai",
                "pertanyaan": "[ESAI 2] Setelah Keraton Kartasura rusak parah akibat Geger Pacinan, ke kota mana keraton dipindahkan pada 1745?",
                "kata_kunci": ["surakarta", "solo"],
                "contoh_benar": "Surakarta"
            }
        ]
    },
    {
        "stage_id": 4,
        "judul": "Stage 4: Pergerakan Nasional",
        "soal": [
            {
                "tipe": "pg",
                "pertanyaan": "Artikel 'Een Eereschuld' (Hutang Kehormatan) yang melatarbelakangi Politik Etis ditulis oleh...",
                "opsi": ["C.Th. van Deventer", "Snouck Hurgronje", "Douwes Dekker"],
                "benar": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Peristiwa luar negeri tahun 1905 yang membuktikan bangsa Asia mampu mengalahkan bangsa Eropa adalah...",
                "opsi": ["Revolusi Tiongkok", "Kemenangan Jepang atas Rusia", "Gerakan Turki Muda"],
                "benar": 1
            },
            {
                "tipe": "pg",
                "pertanyaan": "Organisasi modern pertama yang berdiri pada 20 Mei 1908 di Gedung STOVIA Batavia adalah...",
                "opsi": ["Sarekat Islam", "Indische Partij", "Budi Utomo"],
                "benar": 2
            },
            {
                "tipe": "pg",
                "pertanyaan": "Pendiri Sarekat Dagang Islam (SDI) di Surakarta yang kelak berubah menjadi Sarekat Islam adalah...",
                "opsi": ["H. Samanhudi", "H.O.S. Tjokroaminoto", "Agus Salim"],
                "benar": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Partai politik pertama di Hindia Belanda yang didirikan Tiga Serangkai pada 25 Desember 1912 adalah...",
                "opsi": ["Perhimpunan Indonesia", "Indische Partij", "Parindra"],
                "benar": 1
            },
            {
                "tipe": "pg",
                "pertanyaan": "Artikel karya Suwardi Suryaningrat yang mengkritik perayaan 100 tahun kemerdekaan Belanda berjudul...",
                "opsi": ["Een Eereschuld", "Medan Prijaji", "Als Ik Eens Nederlander Was"],
                "benar": 2
            },
            {
                "tipe": "esai",
                "pertanyaan": "[ESAI 1] Sebutkan salah satu dari 3 isi Trias van Deventer dalam Politik Etis!",
                "kata_kunci": ["irigasi", "edukasi", "emigrasi", "pengairan", "pendidikan", "perpindahan"],
                "contoh_benar": "Irigasi / Edukasi / Emigrasi"
            },
            {
                "tipe": "esai",
                "pertanyaan": "[ESAI 2] Siapa dokter Jawa yang menggalang dana beasiswa (Studiefonds) hingga menginspirasi berdirinya Budi Utomo?",
                "kata_kunci": ["wahidin", "sudirohusodo"],
                "contoh_benar": "Dr. Wahidin Sudirohusodo"
            }
        ]
    }
]

ARRAY_HADIAH = [
    {"nama": "Mahkota Emas", "biaya": 120, "skor": 60},
    {"nama": "Lencana Sejarah", "biaya": 80, "skor": 35},
    {"nama": "Sepatu Kancil", "biaya": 150, "skor": 80},
    {"nama": "Kompas Nusantara", "biaya": 100, "skor": 45},
]

# =====================================================================
# 2. DEF & 3. REKURSIF: Hitung Bonus Combo Koin
# =====================================================================
def hitung_bonus_rekursif(streak):
    if streak <= 0:
        return 0
    return (streak * 10) + hitung_bonus_rekursif(streak - 1)

# =====================================================================
# 4. FOR: Mencari Data Stage dari Array
# =====================================================================
def cari_stage_by_id(stage_id):
    for stage in ARRAY_STAGE:
        if stage["stage_id"] == stage_id:
            return stage
    return None

# =====================================================================
# 5. IF - ELSE: Evaluasi Jawaban (Pilihan Ganda & Esai)
# =====================================================================
def evaluasi_jawaban(stage_id, tahap_idx, jawaban_user, streak):
    stage = cari_stage_by_id(stage_id)
    soal = stage["soal"][tahap_idx]
    is_benar = False

    if soal["tipe"] == "pg":
        if int(jawaban_user) == soal["benar"]:
            is_benar = True
    else:
        teks = str(jawaban_user).strip().lower()
        for kunci in soal["kata_kunci"]:
            if kunci in teks and len(teks) >= 3:
                is_benar = True
                break

    if is_benar:
        streak_baru = streak + 1
        koin_didapat = 50 + hitung_bonus_rekursif(streak_baru)
        return {
            "benar": True,
            "koin_didapat": koin_didapat,
            "streak_baru": streak_baru,
            "pesan": f"Benar! +{koin_didapat} Koin"
        }
    else:
        pesan_salah = "Awas! Buaya membuka mulutnya!"
        if soal["tipe"] == "esai":
            pesan_salah = f"Kurang tepat! Petunjuk: {soal['contoh_benar']}"
        return {
            "benar": False,
            "koin_didapat": 0,
            "streak_baru": 0,
            "pesan": pesan_salah
        }

# =====================================================================
# 6. GREEDY: Menghitung Pecahan Koin Terbesar Lebih Dulu
# =====================================================================
def hitung_pecahan_greedy(total_koin):
    pecahan = [100, 50, 20, 10]
    sisa = total_koin
    hasil = []
    for p in pecahan:
        if sisa >= p:
            jml = sisa // p
            sisa %= p
            hasil.append({"nilai": p, "jumlah": jml})
    return hasil

# =====================================================================
# 7. DYNAMIC PROGRAMMING (0/1 KNAPSACK): Skor Bonus Maksimal
# =====================================================================
def hitung_skor_optimal_dp(budget_koin):
    n = len(ARRAY_HADIAH)
    skala = budget_koin // 10
    dp = [[0 for _ in range(skala + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        biaya = ARRAY_HADIAH[i - 1]["biaya"] // 10
        skor = ARRAY_HADIAH[i - 1]["skor"]
        for w in range(skala + 1):
            if biaya <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - biaya] + skor)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][skala]

# =====================================================================
# ROUTES MULTI-HALAMAN
# =====================================================================
@app.route("/")
def page_start():
    return render_template("start.html")

@app.route("/levels")
def page_levels():
    return render_template("levels.html")

@app.route("/play/<int:stage_id>")
def page_game(stage_id):
    stage = cari_stage_by_id(stage_id)
    if not stage:
        stage = ARRAY_STAGE[0]
    return render_template("game.html", stage_id=stage["stage_id"], stage_judul=stage["judul"])

# =====================================================================
# API ENDPOINTS
# =====================================================================
@app.route("/api/stage/<int:stage_id>", methods=["GET"])
def api_stage(stage_id):
    stage = cari_stage_by_id(stage_id)
    if not stage:
        return jsonify({"error": "Stage tidak ditemukan"}), 404
    return jsonify(stage)

@app.route("/api/jawab", methods=["POST"])
def api_jawab():
    data = request.json
    hasil = evaluasi_jawaban(
        int(data.get("stage_id", 1)),
        int(data.get("tahap", 0)),
        data.get("jawaban", ""),
        int(data.get("streak", 0))
    )
    return jsonify(hasil)

@app.route("/api/beli-hati", methods=["POST"])
def api_beli_hati():
    data = request.json
    nyawa = int(data.get("nyawa", 3))
    total_koin = int(data.get("total_koin", 0))
    harga_hati = 100

    # Jika hati sudah maksimal (3), batalkan pembelian (tidak terjadi apa-apa)
    if nyawa >= 3:
        return jsonify({
            "berhasil": False,
            "batal_maks": True,
            "nyawa_baru": nyawa,
            "koin_baru": total_koin
        })
    elif total_koin < harga_hati:
        return jsonify({
            "berhasil": False,
            "batal_maks": False,
            "pesan": f"Koin tidak cukup! Butuh {harga_hati} koin."
        })
    else:
        return jsonify({
            "berhasil": True,
            "batal_maks": False,
            "nyawa_baru": nyawa + 1,
            "koin_baru": total_koin - harga_hati,
            "pesan": "❤️ +1 Hati berhasil dibeli!"
        })

@app.route("/api/selesai", methods=["POST"])
def api_selesai():
    total_koin = int(request.json.get("total_koin", 0))
    return jsonify({
        "pecahan": hitung_pecahan_greedy(total_koin),
        "skor_bonus": hitung_skor_optimal_dp(total_koin)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)