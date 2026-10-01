"""Modul untuk menghitung luas persegi panjang."""


def hitung_luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang.

    Args:
        panjang: Panjang persegi panjang.
        lebar: Lebar persegi panjang.

    Returns:
        Luas persegi panjang.

    Raises:
        ValueError: Jika panjang atau lebar kurang dari atau sama dengan nol.
    """
    if panjang <= 0 or lebar <= 0:
        raise ValueError("Panjang dan lebar harus lebih besar dari nol.")

    return panjang * lebar


def main() -> None:
    """Menjalankan program utama."""
    panjang = 5.0
    lebar = 3.0

    try:
        luas = hitung_luas_persegi_panjang(panjang, lebar)
        print(f"Luas persegi panjang: {luas}")
    except ValueError as error:
        print(f"Input tidak valid: {error}")


if __name__ == "__main__":
    main()