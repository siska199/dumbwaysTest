def hitungVoucher(jenisVoucher,nominal):
    if jenisVoucher=="DumbWaysJos":
        if nominal == 50000:
            diskon = nominal*21.1/100
            bayar = nominal-diskon
            kembalian = diskon
        elif nominal > 50000:
            diskon = 20000
            bayar = nominal-diskon
            kembalian = diskon
        else:
            return("Penggunaan voucher tidak memenuhi minimal syarat")
                
    elif jenisVoucher=="DumbWaysMantap":
        if nominal == 80000:
            diskon = nominal*30./100
            bayar = nominal-diskon
            kembalian = diskon
        elif nominal > 80000:
            diskon = 40000
            bayar = nominal-diskon
            kembalian = diskon
        else:
            return("Penggunaan voucher tidak memenuhi minimal syarat")
    return( "Uang yang harus dibayar : "+str(bayar)+"\n"
            "Diskon : "+str(diskon)+"\n"
            "Kembalian: "+str(kembalian)
    )


print(hitungVoucher("DumbWaysJos",100000))