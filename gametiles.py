tiles = {
    "s1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "s2": "north"
        }
    },
    "s2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "s1": "south",
            "s3": "north"
        }
    },
    "s3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "s2": "south",
            "s4": "north"
        }
    },
    "s4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "s3": "south",
            "s5": "north"
        }
    },
    "s5": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "s4": "south",
            "c1": "north"
        }
    },
    "g1": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g2": "north"
        }
    },
    "g2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g1": "south",
            "g3": "north"
        }
    },
    "g3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g2": "south",
            "g4": "east"
        }
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
        }
    },
    "g5": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g6": "north"
        }
    },
    "g6": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g5": "south",
            "g7": "north"
        }
    },
    "g7": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g6": "south",
            "g8": "west"
        }
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
        }
    },
    "g9": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g10": "east"
        }
    },
    "g10": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g9": "west",
            "c2": "east"
        }
    },
    "g11": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g12": "west"
        }
    },
    "g12": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g11": "east",
            "c2": "west"
        }
    },
    "g13": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g14": "east"
        }
    },
    "g14": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g13": "west",
            "c6": "east"
        }
    },
    "g15": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g16": "west"
        }
    },
    "g16": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g15": "east",
            "c6": "west"
        }
    },
    "g17": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g18": "west"
        }
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
        }
    },
    "g19": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g20": "east"
        }
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
        }
    },
    "g21": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g22": "west"
        }
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
        }
    },
    "g23": {
        "occupied": False,
        "on fire": False,
        "entrance": True,
        "connected to": {
            "g24": "east"
        }
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
        }
    },
    "c1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "s5": "south",
            "lr1": "east",
            "ll1": "west"
        }
    },
    "c2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g10": "west",
            "g12": "east",
            "c3": "north"
        }
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
        }
    },
    "c4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c3": "south",
            "cl4": "west",
            "c5": "north",
            "cr4": "east"
        }
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
        }
    },
    "c6": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c5": "south",
            "g14": "west",
            "g16": "east"
        }
    },
    "c7": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "g18": "east",
            "g20": "west"
        }
    },
    "c8": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c7": "south",
            "c9": "north"
        }
    },
    "c9": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c8": "south",
            "c10": "north"
        }
    },
    "c10": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c9": "south",
            "ur4": "east",
            "ul4": "west",
            "c11": "north"
        }
    },
    "c11": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c10": "south",
            "c12": "north"
        }
    },
    "c12": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c11": "south",
            "g22": "east",
            "g24": "west"
        }
    },
    "ll1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c1": "east",
            "ll2": "west"
        }
    },
    "ll2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ll1": "east",
            "ll3": "west"
        }
    },
    "ll3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ll2": "east",
            "ll4": "west"
        }
    },
    "ll4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ll3": "east",
            "ll5": "west"
        }
    },
    "ll5": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ll4": "east",
            "g4": "west",
            "l1": "north"
        }
    },
    "lr1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "c1": "west",
            "lr1": "east"
        }
    },
    "lr2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "lr1": "west",
            "lr3": "east"
        }
    },
    "lr3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "lr2": "west",
            "lr4": "east"
        }
    },
    "lr4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "lr3": "west",
            "lr5": "east"
        }
    },
    "lr5": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "lr4": "west",
            "g8": "east",
            "r1": "north"
        }
    },
    "l1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ll5": "south",
            "l2": "north"
        }
    },
    "l2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l1": "south",
            "l3": "north"
        }
    },
    "l3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l2": "south",
            "l4": "north"
        }
    },
    "l4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l3": "south",
            "l5": "north"
        }
    },
    "l5": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l4": "south",
            "l6": "north"
        }
    },
    "l6": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l5": "south",
            "l7": "north",
            "cl1": "east"
        }
    },
    "l7": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l6": "south",
            "l8": "north"
        }
    },
    "l8": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l7": "south",
            "l9": "north"
        }
    },
    "l9": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l8": "south",
            "l10": "north"
        }
    },
    "l10": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l9": "south",
            "l11": "north"
        }
    },
    "l11": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l10": "south",
            "l12": "north"
        }
    },
    "l12": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l11": "south",
            "l13": "north"
        }
    },
    "l13": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l12": "south",
            "ul1": "east"
        }
    },
    "r1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "lr5": "south",
            "r2": "north"
        }
    },
    "r2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r1": "south",
            "r3": "north"
        }
    },
    "r3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r2": "south",
            "r4": "north"
        }
    },
    "r4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r3": "south",
            "r5": "north"
        }
    },
    "r5": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r4": "south",
            "r6": "north"
        }
    },
    "r6": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r5": "south",
            "r7": "north",
            "cr1": "west"
        }
    },
    "r7": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r6": "south",
            "r8": "north"
        }
    },
    "r8": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r7": "south",
            "r9": "north"
        }
    },
    "r9": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r8": "south",
            "r10": "north"
        }
    },
    "r10": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r9": "south",
            "r11": "north"
        }
    },
    "r11": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r10": "south",
            "r12": "north"
        }
    },
    "r12": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r11": "south",
            "r13": "north"
        }
    },
    "r13": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r12": "south",
            "ur1": "west"
        }
    },
    "ul1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l13": "west",
            "ul2": "east"
        }
    },
    "ul2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ul1": "west",
            "ul3": "east"
        }
    },
    "ul3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ul2": "west",
            "ul4": "east"
        }
    },
    "ul4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ul3": "west",
            "c10": "east"
        }
    },
    "ur1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r13": "east",
            "ur2": "west"
        }
    },
    "ur2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ur1": "east",
            "ur3": "west"
        }
    },
    "ur3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ur2": "east",
            "ur4": "west"
        }
    },
    "ur4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "ur3": "east",
            "c10": "west"
        }
    },
    "cl1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "l6": "west",
            "cl2": "east"
        }
    },
    "cl2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "cl1": "west",
            "cl3": "east"
        }
    },
    "cl3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "cl2": "west",
            "cl4": "east"
        }
    },
    "cl4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "cl3": "west",
            "c4": "east"
        }
    },
    "cr1": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "r6": "east",
            "cr2": "west"
        }
    },
    "cr2": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "cr1": "east",
            "cr3": "west"
        }
    },
    "cr3": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "cr2": "east",
            "cr4": "west"
        }
    },
    "cr4": {
        "occupied": False,
        "on fire": False,
        "connected to": {
            "cr3": "east",
            "c4": "west"
        }
    }
}
