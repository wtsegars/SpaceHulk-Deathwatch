import textwrap
import gametiles

def map():
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