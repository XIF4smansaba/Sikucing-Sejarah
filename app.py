from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# =====================================================================
# 1. ARRAY (LIST) - Menyimpan data 4 Stage (6 PG + 2 Esai per Stage)
# =====================================================================
ARRAY_STAGE = [
    {
        "id": 1,
        "judul": "Stage 1: Perang Aceh",
        "soal": [
            {
                "tipe": "pg",
                "pertanyaan": "Ahli Islam Belanda yang meneliti Aceh (1891–1892) dan merumuskan strategi penaklukan Aceh adalah...",
                "opsi": ["Jenderal De Kock", "Snouck Hurgronje", "C.Th. van Deventer"],
                "kunci": 1
            },
            {
                "tipe": "pg",
                "pertanyaan": "Perjanjian tahun 1871 yang memberi kebebasan Belanda menguasai Aceh adalah...",
                "opsi": ["Traktat Sumatera", "Traktat London", "Perjanjian Bongaya"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Pasukan khusus Belanda yang dibentuk untuk menghadapi perang gerilya di Aceh adalah...",
                "opsi": ["KNIL", "Marsose", "Heiho"],
                "kunci": 1
            },
            {
                "tipe": "pg",
                "pertanyaan": "Tokoh pahlawan wanita Aceh yang melanjutkan perjuangan setelah Teuku Umar gugur adalah...",
                "opsi": ["Cut Nyak Dien", "Martha Christina Tiahahu", "Nyi Ageng Serang"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Pernyataan pendek yang dipaksakan Belanda kepada penguasa Aceh agar mengakui kedaulatan Belanda disebut...",
                "opsi": ["Plakat Pendek", "Cultuurstelsel", "Politik Etis"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Jenderal Belanda yang tewas tertembak di depan Masjid Raya Baiturrahman pada tahun 1873 adalah...",
                "opsi": ["Jenderal Van Swieten", "Jenderal J.H.R. Kohler", "Jenderal Van Heutsz"],
                "kunci": 1
            },
            {
                "tipe": "esai",
                "pertanyaan": "Sebutkan nama tokoh pahlawan Aceh yang terkenal dengan siasat berpura-pura menyerah kepada Belanda!",
                "kata_kunci": ["teuku umar", "umar"]
            },
            {
                "tipe": "esai",
                "pertanyaan": "Sebutkan nama masjid bersejarah di Banda Aceh yang menjadi pusat pertahanan rakyat Aceh saat diserang Belanda!",
                "kata_kunci": ["baiturrahman", "masjid raya baiturrahman"]
            }
        ]
    },
    {
        "id": 2,
        "judul": "Stage 2: Perlawanan Banten",
        "soal": [
            {
                "tipe": "pg",
                "pertanyaan": "Sultan Banten yang gigih menentang monopoli perdagangan VOC adalah...",
                "opsi": ["Sultan Ageng Tirtayasa", "Sultan Hasanuddin", "Sultan Agung"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Putra Sultan Ageng Tirtayasa yang diadu domba oleh VOC agar berbalik melawan ayahnya adalah...",
                "opsi": ["Pangeran Diponegoro", "Sultan Haji", "Pangeran Antasari"],
                "kunci": 1
            },
            {
                "tipe": "pg",
                "pertanyaan": "Politik adu domba yang diterapkan VOC untuk memecah belah Kesultanan Banten disebut...",
                "opsi": ["Devide et Impera", "Pax Neerlandica", "Hongi Tochten"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Komoditas utama Kesultanan Banten yang sangat diincar VOC untuk dimonopoli adalah...",
                "opsi": ["Cengkeh", "Lada", "Kopi"],
                "kunci": 1
            },
            {
                "tipe": "pg",
                "pertanyaan": "Benteng pertahanan VOC di Batavia yang sering diserang oleh pasukan Banten terletak di dekat...",
                "opsi": ["Sungai Ciliwung", "Sungai Musi", "Sungai Mahakam"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Setelah Sultan Haji naik takhta dengan bantuan VOC, Banten terpaksa menyerahkan hak monopoli dagang di wilayah...",
                "opsi": ["Lampung", "Maluku", "Ternate"],
                "kunci": 0
            },
            {
                "tipe": "esai",
                "pertanyaan": "Sebutkan nama istana atau keraton Kesultanan Banten yang menjadi pusat pemerintahan Sultan Ageng Tirtayasa!",
                "kata_kunci": ["surosowan", "tirtayasa"]
            },
            {
                "tipe": "esai",
                "pertanyaan": "Siapakah nama panglima perang sekaligus ulama besar dari Makassar yang membantu perjuangan Sultan Ageng Tirtayasa di Banten?",
                "kata_kunci": ["syekh yusuf", "yusuf"]
            }
        ]
    },
    {
        "id": 3,
        "judul": "Stage 3: Geger Pacinan & Diponegoro",
        "soal": [
            {
                "tipe": "pg",
                "pertanyaan": "Peristiwa pembantaian etnis Tionghoa oleh VOC di Batavia pada tahun 1740 dikenal sebagai...",
                "opsi": ["Geger Pacinan", "Perang Padri", "Perang Puputan"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Gubernur Jenderal VOC yang bertanggung jawab atas tragedi Geger Pacinan tahun 1740 adalah...",
                "opsi": ["Jan Pieterszoon Coen", "Adriaan Valckenier", "Herman Willem Daendels"],
                "kunci": 1
            },
            {
                "tipe": "pg",
                "pertanyaan": "Sebab khusus meletusnya Perang Diponegoro (1825–1830) adalah pemasangan patok jalan oleh Belanda yang melintasi...",
                "opsi": ["Makam leluhur Pangeran Diponegoro", "Keraton Surakarta", "Pelabuhan Semarang"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Strategi Belanda untuk mempersempit ruang gerak pasukan Pangeran Diponegoro adalah...",
                "opsi": ["Benteng Stelsel", "Cultuurstelsel", "Contingenten"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Pemimpin pasukan Belanda yang menangkap Pangeran Diponegoro melalui tipu muslihat perundingan di Magelang adalah...",
                "opsi": ["Jenderal De Kock", "Jenderal Van der Capellen", "Jenderal Michiels"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Setelah ditangkap di Magelang pada tahun 1830, Pangeran Diponegoro akhirnya diasingkan ke...",
                "opsi": ["Manado lalu Makassar", "Bengkulu lalu Banda", "Digul lalu Flores"],
                "kunci": 0
            },
            {
                "tipe": "esai",
                "pertanyaan": "Sebutkan nama daerah kediaman Pangeran Diponegoro di Yogyakarta yang menjadi lokasi awal pemasangan patok Belanda!",
                "kata_kunci": ["tegalrejo"]
            },
            {
                "tipe": "esai",
                "pertanyaan": "Sebutkan nama tokoh ulama penasihat spiritual Pangeran Diponegoro selama Perang Jawa!",
                "kata_kunci": ["kyai maja", "kiai maja", "maja"]
            }
        ]
    },
    {
        "id": 4,
        "judul": "Stage 4: Pergerakan Nasional",
        "soal": [
            {
                "tipe": "pg",
                "pertanyaan": "Organisasi modern pertama di Indonesia yang berdiri pada 20 Mei 1908 dan menjadi tonggak Kebangkitan Nasional adalah...",
                "opsi": ["Budi Utomo", "Sarekat Islam", "Indische Partij"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Tiga serangkai pendiri Indische Partij adalah Douwes Dekker, dr. Cipto Mangunkusumo, dan...",
                "opsi": ["Suwardi Suryaningrat", "H.O.S. Tjokroaminoto", "Moh. Hatta"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Organisasi yang awalnya bernama Sarekat Dagang Islam (SDI) didirikan di Solo oleh...",
                "opsi": ["Haji Samanhudi", "K.H. Ahmad Dahlan", "Dr. Sutomo"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Ikrar Sumpah Pemuda yang menyatukan tanah air, bangsa, dan bahasa Indonesia dicetuskan pada tanggal...",
                "opsi": ["28 Oktober 1928", "20 Mei 1908", "17 Agustus 1945"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Lagu kebangsaan 'Indonesia Raya' pertama kali diperdengarkan pada Kongres Pemuda II oleh penciptanya, yaitu...",
                "opsi": ["W.R. Supratman", "Ismail Marzuki", "C. Simanjuntak"],
                "kunci": 0
            },
            {
                "tipe": "pg",
                "pertanyaan": "Partai Nasional Indonesia (PNI) yang bertujuan mencapai Indonesia merdeka didirikan pada tahun 1927 oleh...",
                "opsi": ["Ir. Soekarno", "Sutan Sjahrir", "Tan Malaka"],
                "kunci": 0
            },
            {
                "tipe": "esai",
                "pertanyaan": "Sebutkan nama perguruan pendidikan nasional yang didirikan oleh Ki Hajar Dewantara pada tahun 1922!",
                "kata_kunci": ["taman siswa", "tamansiswa"]
            },
            {
                "tipe": "esai",
                "pertanyaan": "Sebutkan nama ketua panitia Kongres Pemuda II tahun 1928!",
                "kata_kunci": ["sugondo", "soegondo", "djojopoespito", "joyopuspito"]
            }
        ]
    }
]

# Array hadiah untuk perhitungan Dynamic Programming (0/1 Knapsack)
ARRAY_HADIAH = [
    {"nama": "Lencana Perunggu", "harga": 50, "skor": 60},
    {"nama": "Lencana Perak", "harga": 100, "skor": 130},
    {"nama": "Lencana Emas", "harga": 150, "skor": 210},
    {"nama": "Mahkota Sejarah", "harga": 200, "skor": 300}
]


# =====================================================================
# 2. FUNGSI (def) & 3. PERULANGAN (for) - Mencari Stage berdasarkan ID
# =====================================================================
def cari_stage_by_id(stage_id):
    for stage in ARRAY_STAGE:
        if stage["id"] == stage_id:
            return stage
    return ARRAY_STAGE[0]


# =====================================================================
# 4. PERCABANGAN (if - else) - Evaluasi Jawaban PG & Esai
# =====================================================================
def evaluasi_jawaban(soal, jawaban_user):
    if soal["tipe"] == "pg":
        return int(jawaban_user) == soal["kunci"]
    else:
        teks = str(jawaban_user).strip().lower()
        for kata in soal["kata_kunci"]:
            if kata in teks:
                return True
        return False


# =====================================================================
# 5. ALGORITMA GREEDY - Memecah total koin ke pecahan terbesar dahulu
# =====================================================================
def hitung_pecahan_greedy(total_koin):
    pecahan = [100, 50, 20, 10]
    hasil = {}
    sisa = total_koin
    for p in pecahan:
        jumlah = sisa // p
        if jumlah > 0:
            hasil[str(p)] = jumlah
            sisa = sisa % p
    return hasil


# =====================================================================
# 6. REKURSIF - Menghitung bonus beruntun dengan pemanggilan diri sendiri
# =====================================================================
def hitung_bonus_rekursif(streak):
    if streak <= 0:
        return 0
    return 5 + hitung_bonus_rekursif(streak - 1)


# =====================================================================
# 7. DYNAMIC PROGRAMMING (0/1 Knapsack) - Skor bonus optimal dari koin
# =====================================================================
def hitung_skor_optimal_dp(budget_koin):
    n = len(ARRAY_HADIAH)
    kapasitas = min(budget_koin, 400)
    dp = [[0 for _ in range(kapasitas + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        harga = ARRAY_HADIAH[i - 1]["harga"]
        skor = ARRAY_HADIAH[i - 1]["skor"]
        for w in range(kapasitas + 1):
            if harga <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - harga] + skor)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][kapasitas]


# =====================================================================
# RUTE HALAMAN WEB (FLASK)
# =====================================================================
@app.route("/")
def halaman_start():
    return render_template("start.html")


@app.route("/levels")
def halaman_levels():
    return render_template("levels.html", stages=ARRAY_STAGE)


@app.route("/play/<int:stage_id>")
def halaman_play(stage_id):
    stage = cari_stage_by_id(stage_id)
    return render_template("game.html", stage_id=stage["id"], stage_judul=stage["judul"])


# =====================================================================
# API ENDPOINTS
# =====================================================================
@app.route("/api/stage/<int:stage_id>")
def api_get_stage(stage_id):
    stage = cari_stage_by_id(stage_id)
    soal_aman = []
    for s in stage["soal"]:
        if s["tipe"] == "pg":
            soal_aman.append({
                "tipe": "pg",
                "pertanyaan": s["pertanyaan"],
                "opsi": s["opsi"]
            })
        else:
            soal_aman.append({
                "tipe": "esai",
                "pertanyaan": s["pertanyaan"]
            })
    return jsonify({"id": stage["id"], "judul": stage["judul"], "soal": soal_aman})


@app.route("/api/jawab", methods=["POST"])
def api_jawab():
    data = request.get_json()
    stage = cari_stage_by_id(int(data.get("stage_id", 1)))
    tahap = int(data.get("tahap", 0))
    jawaban_user = data.get("jawaban")
    streak = int(data.get("streak", 0))

    soal = stage["soal"][tahap]
    benar = evaluasi_jawaban(soal, jawaban_user)

    if benar:
        streak_baru = streak + 1
        _ = hitung_bonus_rekursif(streak_baru)  # Tetap memanggil fungsi Rekursif
        koin_didapat = 50
        pesan = "Benar! +50 Koin"
    else:
        streak_baru = 0
        koin_didapat = 0
        pesan = "Salah! Nyawa berkurang 1 ❤️"

    return jsonify({
        "benar": benar,
        "koin_didapat": koin_didapat,
        "streak_baru": streak_baru,
        "pesan": pesan
    })


@app.route("/api/beli-hati", methods=["POST"])
def api_beli_hati():
    data = request.get_json()
    nyawa = int(data.get("nyawa", 3))
    total_koin = int(data.get("total_koin", 0))
    harga_hati = 100

    if nyawa >= 3:
        return jsonify({
            "berhasil": False,
            "batal_maks": True,
            "nyawa_baru": nyawa,
            "koin_baru": total_koin,
            "pesan": "Nyawa sudah penuh!"
        })
    elif total_koin >= harga_hati:
        return jsonify({
            "berhasil": True,
            "batal_maks": False,
            "nyawa_baru": nyawa + 1,
            "koin_baru": total_koin - harga_hati,
            "pesan": "Berhasil beli +1 Hati! ❤️"
        })
    else:
        return jsonify({
            "berhasil": False,
            "batal_maks": False,
            "nyawa_baru": nyawa,
            "koin_baru": total_koin,
            "pesan": "Koin tidak cukup! Butuh 100 Koin."
        })


@app.route("/api/selesai", methods=["POST"])
def api_selesai():
    data = request.get_json()
    total_koin = int(data.get("total_koin", 0))
    pecahan_greedy = hitung_pecahan_greedy(total_koin)
    skor_dp = hitung_skor_optimal_dp(total_koin)

    return jsonify({
        "pecahan_greedy": pecahan_greedy,
        "skor_optimal_dp": skor_dp
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
