from textwrap import dedent
import gametiles
import squad
import genestealers
import radarblips

def map():
        s1 = None
        s2 = None
        s3 = None
        s4 = None
        s5 = None
        g1 = None
        g2 = None
        g3 = None
        g4 = None
        g5 = None
        g6 = None
        g7 = None
        g8 = None
        g9 = None
        g10 = None
        g11 = None
        g12 = None
        g13 = None
        g14 = None
        g15 = None
        g16 = None
        g17 = None
        g18 = None
        g19 = None
        g20 = None
        g21 = None
        g22 = None
        g23 = None
        g24 = None
        c1 = None
        c2 = None
        c3 = None
        c4 = None
        c5 = None
        c6 = None
        c7 = None
        c8 = None
        c9 = None
        c10 = None
        c11 = None
        c12 = None
        ll1 = None
        ll2 = None
        ll3 = None
        ll4 = None
        ll5 = None
        lr1 = None
        lr2 = None
        lr3 = None
        lr4 = None
        lr5 = None
        l1 = None
        l2 = None
        l3 = None
        l4 = None
        l5 = None
        l6 = None
        l7 = None
        l8 = None
        l9 = None
        l10 = None
        l11 = None
        l12 = None
        l13 = None
        r1 = None
        r2 = None
        r3 = None
        r4 = None
        r5 = None
        r6 = None
        r7 = None
        r8 = None
        r9 = None
        r10 = None
        r11 = None
        r12 = None
        r13 = None
        ul1 = None
        ul2 = None
        ul3 = None
        ul4 = None
        ur1 = None
        ur2 = None
        ur3 = None
        ur4 = None
        cl1 = None
        cl2 = None
        cl3 = None
        cl4 = None
        cr1 = None
        cr2 = None
        cr3 = None
        cr4 = None

        tiles_list = [s1, s2, s3, s4, s5, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22, g23, g24, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, ll1, ll2, ll3, ll4, ll5, lr1, lr2, lr3, lr4, lr5, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, ul1, ul2, ul3, ul4, ur1, ur2, ur3 , ur4, cl1, cl2, cl3, cl4, cr1, cr2, cr3, cr4]

        for x in tiles_list:
                for y in gametiles.tiles:
                        if gametiles.tiles[y]["occupied"] == True:
                                if gametiles.tiles[y]["on fire"] == True:
                                        tiles_list[x] = "FF"
                                elif gametiles.tiles[y]["door"]:
                                        if gametiles.tiles[y]["door"]["sealed"] == True:
                                                if gametiles.tiles[y] == "g4" or gametiles.tiles[y] == "g8" or gametiles.tiles[y] == "g20" or gametiles.tiles[y] == "g18" or gametiles.tiles[y] == "g22" or gametiles.tiles[y] == "g24":
                                                        tiles_list[x] = "II "
                                                        break
                                                elif gametiles.tiles[y] == "c3" or gametiles.tiles[y] == "c5":
                                                        tiles_list[x] = "-- "
                                                        break
                                else:
                                        for z in squad.squad:
                                                if squad.squad[z]["current_place"] == gametiles.tiles[y]:
                                                        if squad.squad[z]["direction"] == "north":
                                                                tiles_list[x] = f"^{z + 1}"
                                                                break
                                                        elif squad.squad[z]["direction"] == "south":
                                                                tiles_list[x] = f"v{z + 1}"
                                                                break
                                                        elif squad.squad[z]["direction"] == "east":
                                                                tiles_list[x] = f">{z + 1}"
                                                                break
                                                        elif squad.squad[z]["direction"] == "west":
                                                                tiles_list[x] = f"<{z + 1}"
                                                                break
                                        for z in genestealers.genestealers:
                                                if genestealers.genestealers[z]["current_place"] == gametiles.tiles[y]:
                                                        tiles_list[x] = "G  "
                                                        break
                                        for z in radarblips.blips:
                                                if radarblips.blips[z]["current_place"] == gametiles.tiles[y]:
                                                        tiles_list[x] = "O "
                                                        break
                        else:
                                tiles_list[x] = "  "
        print(dedent (f"""                            ===[{g23}][{g24}][{c12}][{g22}][{g21}]===
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
                        """))
