from datetime import datetime

def sahkan_input(nama, nokp):

    if not nama.strip():
        return False, "Nama tidak boleh kosong."

    if len(nokp) != 12 or not nokp.isdigit():
        return False, "Nombor kad pengenalan mestilah 12 digit angka."

    tarikh_str = nokp[:6]

    try:
        datetime.strptime(tarikh_str, "%y%m%d")
    except ValueError:
        return False, "6 digit pertama No. KP mestilah tarikh yang sah (YYMMDD)."

    return True, ""


def dapatkan_nama_berformat(nama, nokp):

    digit_terakhir = int(nokp[-1])

    if digit_terakhir % 2 != 0:
        gelaran = "Encik"
    else:
        gelaran = "Cik"

    return f"{gelaran} {nama}"


def kira_umur(nokp):

    yy = int(nokp[:2])
    mm = int(nokp[2:4])

    sekarang = datetime.now()
    tahun_semasa = sekarang.year
    bulan_semasa = sekarang.month

    dua_digit_tahun_semasa = tahun_semasa % 100

    if yy <= dua_digit_tahun_semasa:
        tahun_lahir = 2000 + yy
    else:
        tahun_lahir = 1900 + yy

    jumlah_bulan_semasa = (tahun_semasa * 12) + bulan_semasa
    jumlah_bulan_lahir = (tahun_lahir * 12) + mm
    perbezaan_bulan = jumlah_bulan_semasa - jumlah_bulan_lahir

    tahun_umur = perbezaan_bulan // 12
    bulan_umur = perbezaan_bulan % 12

    return f"Anda berumur {tahun_umur} tahun {bulan_umur} bulan"


# ==========================
# Program Utama
# ==========================

if __name__ == "__main__":

    nama = input("Masukkan nama: ")
    nokp = input("Masukkan No. Kad Pengenalan (12 digit): ")

    sah, mesej = sahkan_input(nama, nokp)

    if sah:
        print("\n===== KEPUTUSAN =====")
        print(dapatkan_nama_berformat(nama, nokp))
        print(kira_umur(nokp))
    else:
        print("\nRalat:", mesej)