import textwrap
import gametiles
import squad

def map():
        s1 = gametiles.tiles[0]
        s2 = gametiles.tiles[1]
        s3 = gametiles.tiles[2]
        s4 = gametiles.tiles[3]
        s5 = gametiles.tiles[4]
        g1 = gametiles.tiles[5]
        g2 = gametiles.tiles[6]
        g3 = gametiles.tiles[7]
        g4 = gametiles.tiles[8]
        g5 = gametiles.tiles[9]
        g6 = gametiles.tiles[10]
        g7 = gametiles.tiles[11]
        g8 = gametiles.tiles[12]
        g9 = gametiles.tiles[13]
        g10 = gametiles.tiles[14]
        g11 = gametiles.tiles[15]
        g12 = gametiles.tiles[16]
        g13 = gametiles.tiles[17]
        g14 = gametiles.tiles[18]
        g15 = gametiles.tiles[19]
        g16 = gametiles.tiles[20]
        g17 = gametiles.tiles[21]
        g18 = gametiles.tiles[22]
        g19 = gametiles.tiles[23]
        g20 = gametiles.tiles[24]
        g21 = gametiles.tiles[25]
        g22 = gametiles.tiles[26]
        g23 = gametiles.tiles[27]
        g24 = gametiles.tiles[28]
        c1 = gametiles.tiles[29]
        c2 = gametiles.tiles[30]
        c3 = gametiles.tiles[31]
        c4 = gametiles.tiles[32]
        c5 = gametiles.tiles[33]
        c6 = gametiles.tiles[34]
        c7 = gametiles.tiles[35]
        c8 = gametiles.tiles[36]
        c9 = gametiles.tiles[37]
        c10 = gametiles.tiles[38]
        c11 = gametiles.tiles[39]
        c12 = gametiles.tiles[40]
        ll1 = gametiles.tiles[41]
        ll2 = gametiles.tiles[42]
        ll3 = gametiles.tiles[43]
        ll4 = gametiles.tiles[44]
        ll5 = gametiles.tiles[45]
        lr1 = gametiles.tiles[46]
        lr2 = gametiles.tiles[47]
        lr3 = gametiles.tiles[48]
        lr4 = gametiles.tiles[49]
        lr5 = gametiles.tiles[50]
        l1 = gametiles.tiles[51]
        l2 = gametiles.tiles[52]
        l3 = gametiles.tiles[53]
        l4 = gametiles.tiles[54]
        l5 = gametiles.tiles[55]
        l6 = gametiles.tiles[56]
        l7 = gametiles.tiles[57]
        l8 = gametiles.tiles[58]
        l9 = gametiles.tiles[59]
        l10 = gametiles.tiles[60]
        l11 = gametiles.tiles[61]
        l12 = gametiles.tiles[62]
        l13 = gametiles.tiles[63]
        r1 = gametiles.tiles[64]
        r2 = gametiles.tiles[65]
        r3 = gametiles.tiles[66]
        r4 = gametiles.tiles[67]
        r5 = gametiles.tiles[68]
        r6 = gametiles.tiles[69]
        r7 = gametiles.tiles[70]
        r8 = gametiles.tiles[71]
        r9 = gametiles.tiles[72]
        r10 = gametiles.tiles[73]
        r11 = gametiles.tiles[74]
        r12 = gametiles.tiles[75]
        r13 = gametiles.tiles[76]
        ul1 = gametiles.tiles[77]
        ul2 = gametiles.tiles[78]
        ul3 = gametiles.tiles[79]
        ul4 = gametiles.tiles[80]
        ur1 = gametiles.tiles[81]
        ur2 = gametiles.tiles[82]
        ur3 = gametiles.tiles[83]
        ur4 = gametiles.tiles[84]
        cl1 = gametiles.tiles[85]
        cl2 = gametiles.tiles[86]
        cl3 = gametiles.tiles[87]
        cl4 = gametiles.tiles[88]
        cr1 = gametiles.tiles[89]
        cr2 = gametiles.tiles[90]
        cr3 = gametiles.tiles[91]
        cr4 = gametiles.tiles[92]

        tiles_list = [s1, s2, s3, s4, s5, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22, g23, g24, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, ll1, ll2, ll3, ll4, ll5, lr1, lr2, lr3, lr4, lr5, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, ul1, ul2, ul3, ul4, ur1, ur2, ur3 , ur4, cl1, cl2, cl3, cl4, cr1, cr2, cr3, cr4]

        for x in tiles_list:
                
    print(dedent f"""                            ===[{g23}][{g24}][{c12}][{g22}][{g21}]===
                                                                  [{c11}]
                               [{l13}][{ul1}][{ul2}][{ul3}][{ul4}][{c10}][{ur4}][{ur3}][{ur2}][{ur1}][{r13}]
                               [{l12}]                            [{c9 }]                            [{r12}]
                               [{l11}]                            [{c8 }]                            [{r11}]
                               [{l10}]           ===[{g19}][{g20}][{c7 }][{g18}][{g17}]===           [{r10}]
                               [{l9 }]                 ||                         ||                 [{r9 }]
                               [{l8 }]              [{g13}][{g14}][{c6 }][{g16}][{g15}]              [{r8 }]
                               [{l7 }]                            [{c5 }]                            [{r7 }]
                               [{l6 }][{cl1}][{cl2}][{cl3}][{cl4}][{c4 }][{cr4}][{cr3}][{cr2}][{cr1}][{r6 }]
                               [{l5 }]                            [{c3 }]                            [{r5 }]
                               [{l4 }]              [{g9 }][{g10}][{c2 }][{g12}][{g11}]              [{r4 }]
                               [{l3 }]                ||                           ||                [{r3 }]
                               [{l2 }]                                                               [{r2 }]
                               [{l1 }]                                                               [{r1 }]
                 [{g3 }][{g4 }][{ll5}][{ll4}][{ll3}][{ll2}][{ll1}][{c1 }][{lr1}][{lr2}][{lr3}][{lr4}][{lr5}][{g8 }][{g7 }]
                 [{g2 }]                                          [{s5 }]                                          [{g6 }]
                 [{g1 }]                                          [{s4 }]                                          [{g5 }]
                   ||                                             [{s3 }]                                             ||
                                                                  [{s2 }]
                                                                  [{s1 }]
            legend:
            ^ = Marine facing north
            v = Marine facing south
            > = Marine facing east
            < = Marine facing west
            number next to arrow = Marine in squad
            O = radar blip
            G = Genestealer
            || = Genestealer entrance (facing north or south)
            === = Genestealer entrance (facing east or west)
            II = Closed door (facing east or west)
            -- = Closed door (facing north or south)
            FF = Panel on fire
    """)