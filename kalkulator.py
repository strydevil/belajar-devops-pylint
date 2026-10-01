"""Modul untuk menghitung luas persegi panjang."""


def hitung_luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang.

    Args:
        panjang: Panjang persegi panjang.
        lebar: Lebar persegi panjang.

    Returns:
        Luas persegi panjang.
    """
    return panjang * lebar


def main() -> None:
    """Menjalankan program utama."""
    panjang = 5.0
    lebar = 3.0
    luas = hitung_luas_persegi_panjang(panjang, lebar)
    print(f"Luas persegi panjang: {luas}")


if __name__ == "__main__":
    main()