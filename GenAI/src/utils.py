import re
import json

def process_sku_to_json(sku_string):
    # Dictionary structure based on your 8 blocks
    structured_data = {
        "sku_raw": sku_string,
        "catalog_id": None,
        "shape": None,
        "dimensions": [],
        "lumen": None,
        "voltage": None,
        "cct":None,
        "cri": None,
        "finish": None,
        "mounting": None,
        "options_accessories": [],
        "unclassified_tokens": []
    }
    
    tokens = sku_string.split()
    if not tokens:
        return structured_data

    # 1. Catalog ID (Usually the first part)
    structured_data["catalog_id"] = tokens[0]

    # Patterns based on your Technical Manuals
    patterns = {
        "shape": r"^(TRI|TPP|LPP|ZPP|CIRC|OCT|RPP|QDP)$",
        "lumen": r"^\d+LMF$",
        "voltage": r"^(\d+V|MVOLT)$",
        "cct": r"^\d+K$",
        "cri": r"^\d+CRI$",
        "dimensions": r"^[A-E]\d+(FT|INCH)|(\d+C)$",
        "finish": r"^(BLKT|WCR|WHTCY|WHT)$",
        "mounting": r"^(F2/72A)$"        
    }

    for token in tokens[1:]:
        matched = False
        
        # Check against known patterns
        if re.match(patterns["shape"], token):
            structured_data["shape"] = token
            matched = True
        elif re.match(patterns["lumen"], token):
            structured_data["lumen"] = token
            matched = True
        elif re.match(patterns["voltage"], token):
            structured_data["voltage"] = token
            matched = True
        elif re.match(patterns["cri"], token):
            structured_data["cri"] = token
            matched = True
        elif re.match(patterns["dimensions"], token):
            structured_data["dimensions"].append(token)
            matched = True
        elif re.match(patterns["cct"], token):
            structured_data["cct"] = token
            matched = True
        elif re.match(patterns["finish"], token):
            structured_data["finish"] = token
            matched = True
        elif re.match(patterns["mounting"], token):
            structured_data["mounting"] = token
            matched = True
        # Check for known Accessories/Sensors (SCT, MIN1, ZT, RDCY, etc.)
        elif token in ["SCT", "MIN1", "FLL", "PIRS", "DTCH", "ZT", "RDCY", "APDT12"]:
            structured_data["options_accessories"].append(token)
            matched = True
        
        # If no pattern matches, flag for Step 2 (LLM)
        if not matched:
            structured_data["unclassified_tokens"].append(token)
            
    return structured_data


process_sku_to_json('Q4PDMP RPP A3FT B11FT 90C MIN1 40K 1000LMF 84CRI WHT 347V ZT FLL')