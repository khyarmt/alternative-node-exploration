def assign_sector_code(subsector_code):
    if subsector_code >= "01" and subsector_code <= "05":
        return "A"
    elif subsector_code >= "06" and subsector_code <= "07":
        return "B"
    elif subsector_code >= "08" and subsector_code <= "09":
        return "C"
    elif subsector_code >= "10" and subsector_code <= "13":
        return "D"
    elif subsector_code >= "15" and subsector_code <= "17":
        return "E"
    elif subsector_code >= "19" and subsector_code <= "39":
        return "F"
    elif subsector_code >= "40" and subsector_code <= "49":
        return "G"
    elif subsector_code >= "50" and subsector_code <= "57":
        return "H"
    elif subsector_code == "59":
        return "I"
    elif subsector_code >= "61" and subsector_code <= "68":
        return "J"
    elif subsector_code >= "70" and subsector_code <= "73":
        return "K"
    elif subsector_code >= "74" and subsector_code <= "96":
        return "L"
    elif subsector_code >= "97" and subsector_code <= "98":
        return "M"
    elif subsector_code == "99":
        return "N"
