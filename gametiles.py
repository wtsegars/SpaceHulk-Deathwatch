tiles = {
    "s1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "s2": "north"
        },
        "id_1" : 0
    },
    "s2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "s1": "south",
            "s3": "north"
        },
        "id_1" : 1
    },
    "s3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "s2": "south",
            "s4": "north"
        },
        "id_1" : 2
    },
    "s4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "s3": "south",
            "s5": "north"
        },
        "id_1" : 3
    },
    "s5": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "s4": "south",
            "c1": "north"
        },
        "id_1" : 4
    },
    "g1": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g2": "north"
        },
        "id_1" : 2
    },
    "g2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g1": "south",
            "g3": "north"
        },
        "id_1" : 1
    },
    "g3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g2": "south",
            "g4": "east"
        },
        "id_1" : 0,
        "id_2" : 0
    },
    "g4": {
        "occupied": False,
        "on fire": False,
        "door": {
            "sealed": False
        },
        "connected to": {
            "g3": "west",
            "ll5": "east"
        },
        "id_1" : 1
    },
    "g5": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g6": "north"
        },
        "id_1" : 2
    },
    "g6": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g5": "south",
            "g7": "north"
        },
        "id_1" : 1
    },
    "g7": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g6": "south",
            "g8": "west"
        },
        "id_1" : 14,
        "id_1" : 0
    },
    "g8": {
        "occupied": False,
        "on fire": False,
        "door": {
            "sealed": False
        },
        "connected to": {
            "g7": "east",
            "lr5": "west"
        },
        "id_1" : 13
    },
    "g9": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g10": "east"
        },
        "id_1" : 0
    },
    "g10": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g9": "west",
            "c2": "east"
        },
        "id_1" : 1
    },
    "g11": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g12": "west"
        },
        "id_1" : 4
    },
    "g12": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g11": "east",
            "c2": "west"
        },
        "id_1" : 3
    },
    "g13": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g14": "east"
        },
        "id_1" : 0
    },
    "g14": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g13": "west",
            "c6": "east"
        },
        "id_1" : 1
    },
    "g15": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g16": "west"
        },
        "id_1" : 4
    },
    "g16": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g15": "east",
            "c6": "west"
        },
        "id_1" : 3
    },
    "g17": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g18": "west"
        },
        "id_1" : 4
    },
    "g18": {
        "occupied": False,
        "on fire": False,
        "door": {
            "sealed": False
        },
        "connected to": {
            "g17": "east",
            "c7": "west"
        },
        "id_1" : 3
    },
    "g19": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g20": "east"
        },
        "id_1" : 0
    },
    "g20": {
        "occupied": False,
        "on fire": False,
        "door": {
            "sealed": False
        },
        "connected to": {
            "g19": "west",
            "c7": "east"
        },
        "id_1" : 1
    },
    "g21": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g22": "west"
        },
        "id_1" : 4
    },
    "g22": {
        "occupied": False,
        "on fire": False,
        "door": {
            "sealed": False
        },
        "connected to": {
            "g21": "east",
            "c12": "west"
        },
        "id_1" : 3
    },
    "g23": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g24": "east"
        },
        "id_1" : 0
    },
    "g24": {
        "occupied": False,
        "on fire": False,
        "door": {
            "sealed": False
        },
        "connected to": {
            "g23": "west",
            "c12": "east"
        },
        "id_1" : 1
    },
    "c1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "s5": "south",
            "lr1": "east",
            "ll1": "west"
        },
        "id_1" : 5,
        "id_2" : 7
    },
    "c2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g10": "west",
            "g12": "east",
            "c3": "north"
        },
        "id_1" : 0,
        "id_2" : 2
    },
    "c3": {
        "occupied": False,
        "on fire": False,
        "door": {
            "sealed": False
        },
        "connected to": {
            "c2": "south",
            "c4": "norht"
        },
        "id_1" : 1
    },
    "c4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c3": "south",
            "cl4": "west",
            "c5": "north",
            "cr4": "east"
        },
        "id_1" : 5,
        "id_2" : 2
    },
    "c5": {
        "occupied": False,
        "on fire": False,
        "door": {
            "sealed": False
        },
        "connected to": {
            "c4": "south",
            "c6": "north"
        },
        "id_1" : 3
    },
    "c6": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c5": "south",
            "g14": "west",
            "g16": "east"
        },
        "id_1" : 4,
        "id_2" : 2
    },
    "c7": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g18": "east",
            "g20": "west"
        },
        "id_1" : 0,
        "id_2" : 2
    },
    "c8": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c7": "south",
            "c9": "north"
        },
        "id_1" : 1
    },
    "c9": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c8": "south",
            "c10": "north"
        },
        "id_1" : 2
    },
    "c10": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c9": "south",
            "ur4": "east",
            "ul4": "west",
            "c11": "north"
        },
        "id_1" : 3,
        "id_2" : 5
    },
    "c11": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c10": "south",
            "c12": "north"
        },
        "id_1" : 4
    },
    "c12": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c11": "south",
            "g22": "east",
            "g24": "west"
        },
        "id_1" : 5,
        "id_2" : 2
    },
    "ll1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c1": "east",
            "ll2": "west"
        },
        "id_1" : 6
    },
    "ll2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ll1": "east",
            "ll3": "west"
        },
        "id_1" : 5
    },
    "ll3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ll2": "east",
            "ll4": "west"
        },
        "id_1" : 4
    },
    "ll4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ll3": "east",
            "ll5": "west"
        },
        "id_1" : 3
    },
    "ll5": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ll4": "east",
            "g4": "west",
            "l1": "north"
        },
        "id_1" : 2,
        "id_2" : 0
    },
    "lr1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c1": "west",
            "lr1": "east"
        },
        "id_1" : 8
    },
    "lr2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "lr1": "west",
            "lr3": "east"
        },
        "id_1" : 9
    },
    "lr3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "lr2": "west",
            "lr4": "east"
        },
        "id_1" : 10
    },
    "lr4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "lr3": "west",
            "lr5": "east"
        },
        "id_1" : 11
    },
    "lr5": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "lr4": "west",
            "g8": "east",
            "r1": "north"
        },
        "id_1" : 12,
        "id_2" : 0
    },
    "l1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ll5": "south",
            "l2": "north"
        },
        "id_1" : 1
    },
    "l2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l1": "south",
            "l3": "north"
        },
        "id_1" : 2
    },
    "l3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l2": "south",
            "l4": "north"
        },
        "id_1" : 3
    },
    "l4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l3": "south",
            "l5": "north"
        },
        "id_1" : 4
    },
    "l5": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l4": "south",
            "l6": "north"
        },
        "id_1" : 5
    },
    "l6": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l5": "south",
            "l7": "north",
            "cl1": "east"
        },
        "id_1" : 6,
        "id_1" : 0
    },
    "l7": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l6": "south",
            "l8": "north"
        },
        "id_1" : 7
    },
    "l8": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l7": "south",
            "l9": "north"
        },
        "id_1" : 8
    },
    "l9": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l8": "south",
            "l10": "north"
        },
        "id_1" : 9
    },
    "l10": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l9": "south",
            "l11": "north"
        },
        "id_1" : 10
    },
    "l11": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l10": "south",
            "l12": "north"
        },
        "id_1" : 11
    },
    "l12": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l11": "south",
            "l13": "north"
        },
        "id_1" : 12
    },
    "l13": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l12": "south",
            "ul1": "east"
        },
        "id_1" : 13,
        "id_2" : 0
    },
    "r1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "lr5": "south",
            "r2": "north"
        },
        "id_1" : 1
    },
    "r2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r1": "south",
            "r3": "north"
        },
        "id_1" : 2
    },
    "r3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r2": "south",
            "r4": "north"
        },
        "id_1" : 3
    },
    "r4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r3": "south",
            "r5": "north"
        },
        "id_1" : 4
    },
    "r5": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r4": "south",
            "r6": "north"
        },
        "id_1" : 5
    },
    "r6": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r5": "south",
            "r7": "north",
            "cr1": "west"
        },
        "id_1" : 6,
        "id_2" : 10
    },
    "r7": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r6": "south",
            "r8": "north"
        },
        "id_1" : 7
    },
    "r8": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r7": "south",
            "r9": "north"
        },
        "id_1" : 8
    },
    "r9": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r8": "south",
            "r10": "north"
        },
        "id_1" : 9
    },
    "r10": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r9": "south",
            "r11": "north"
        },
        "id_1" : 10
    },
    "r11": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r10": "south",
            "r12": "north"
        },
        "id_1" : 11
    },
    "r12": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r11": "south",
            "r13": "north"
        },
        "id_1" : 12
    },
    "r13": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r12": "south",
            "ur1": "west"
        },
        "id_1" : 13
    },
    "ul1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l13": "west",
            "ul2": "east"
        },
        "id_1" : 1
    },
    "ul2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ul1": "west",
            "ul3": "east"
        },
        "id_1" : 2
    },
    "ul3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ul2": "west",
            "ul4": "east"
        },
        "id_1" : 3
    },
    "ul4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ul3": "west",
            "c10": "east"
        },
        "id_1" : 4
    },
    "ur1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r13": "east",
            "ur2": "west"
        },
        "id_1" : 9
    },
    "ur2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ur1": "east",
            "ur3": "west"
        },
        "id_1" : 8
    },
    "ur3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ur2": "east",
            "ur4": "west"
        },
        "id_1" : 7
    },
    "ur4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ur3": "east",
            "c10": "west"
        },
        "id_1" : 6
    },
    "cl1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l6": "west",
            "cl2": "east"
        },
        "id_1" : 1
    },
    "cl2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "cl1": "west",
            "cl3": "east"
        },
        "id_1" : 2
    },
    "cl3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "cl2": "west",
            "cl4": "east"
        },
        "id_1" : 3
    },
    "cl4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "cl3": "west",
            "c4": "east"
        },
        "id_1" : 4
    },
    "cr1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r6": "east",
            "cr2": "west"
        },
        "id_1" : 9
    },
    "cr2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "cr1": "east",
            "cr3": "west"
        },
        "id_1" : 8
    },
    "cr3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "cr2": "east",
            "cr4": "west"
        },
        "id_1" : 7
    },
    "cr4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "cr3": "east",
            "c4": "west"
        },
        "id_1" : 6
    }
}
