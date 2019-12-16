tiles = {
    "starting tiles": {
        "s1": {
            "connected to": {
                "s2": "north"
            }
        },
        "s2": {
            "connected to": {
                "s1": "south",
                "s3": "north"
            }
        },
        "s3": {
            "connected to": {
                "s2": "south",
                "s4": "north"
            }
        },
        "s4": {
            "connected to": {
                "s3": "south",
                "s5": "north"
            }
        },
        "s5": {
            "connected to": {
                "s4": "south",
                "c1": "north"
            }
        }
    },
    "genestealer tiles": {
        "g1": {
            "entrance": True,
            "connected to": {
                "g2": "north"
            }
        },
        "g2": {
            "connected to": {
                "g1": "south",
                "g3": "north"
            }
        },
        "g3": {
            "connected to": {
                "g2": "south",
                "g4": "east"
            }
        },
        "g4": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "g3": "west",
                "ll5": "east"
            }
        },
        "g5": {
            "entrance": True,
            "connected to": {
                "g6": "north"
            }
        },
        "g6": {
            "connected to": {
                "g5": "south",
                "g7": "north"
            }
        },
        "g7": {
            "connected to": {
                "g6": "south",
                "g8": "west"
            }
        },
        "g8": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "g7": "east",
                "lr5": "west"
            }
        },
        "g9": {
            "entrance": True,
            "connected to": {
                "g10": "east"
            }
        },
        "g10": {
            "connected to": {
                "g9": "west",
                "c2": "east"
            }
        },
        "g11": {
            "entrance": True,
            "connected to": {
                "g12": "west"
            }
        },
        "g12": {
            "connected to": {
                "g11": "east",
                "c2": "west"
            }
        },
        "g13": {
            "entrance": True,
            "connected to": {
                "g14": "east"
            }
        },
        "g14": {
            "connected to": {
                "g13": "west",
                "c6": "east"
            }
        },
        "g15": {
            "entrance": True,
            "connected to": {
                "g16": "west"
            }
        },
        "g16": {
            "connected to": {
                "g15": "east",
                "c6": "west"
            }
        },
        "g17": {
            "entrance": True,
            "connected to": {
                "g18": "west"
            }
        },
        "g18": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "g17": "east",
                "c7": "west"
            }
        },
        "g19": {
            "entrance": True,
            "connected to": {
                "g20": "east"
            }
        },
        "g20": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "g19": "west",
                "c7": "east"
            }
        },
        "g21": {
            "entrance": True,
            "connected to": {
                "g22": "west"
            }
        },
        "g22": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "g21": "east",
                "c12": "west"
            }
        },
        "g23": {
            "entrance": True,
            "connected to": {
                "g24": "east"
            }
        },
        "g24": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "g23": "west",
                "c12": "east"
            }
        }
    },
    "center tiles": {
        "c1": {
            "connected to": {
                "s5": "south",
                "lr1": "east",
                "ll1": "west"
            }
        },
        "c2": {
            "connected to": {
                "g10": "west",
                "g12": "east",
                "c3": "north"
            }
        },
        "c3": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "c2": "south",
                "c4": "norht"
            }
        },
        "c4": {
            "connected to": {
                "c3": "south",
                "cl4": "west",
                "c5": "north",
                "cr4": "east"
            }
        },
        "c5": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "c4": "south",
                "c6": "north"
            }
        },
        "c6": {
            "connected to": {
                "c5": "south",
                "g14": "west",
                "g16": "east"
            }
        },
        "c7": {
            "connected to": {
                "g18": "east",
                "g20": "west"
            }
        },
        "c8": {
            "connected to": {
                "c7": "south",
                "c9": "north"
            }
        },
        "c9": {
            "connected to": {
                "c8": "south",
                "c10": "north"
            }
        },
        "c10": {
            "connected to": {
                "c9": "south",
                "ur4": "east",
                "ul4": "west",
                "c11": "north"
            }
        },
        "c11": {
            "connected to": {
                "c10": "south",
                "c12": "north"
            }
        },
        "c12": {
            "connected to": {
                "c11": "south",
                "g22": "east",
                "g24": "west"
            }
        }
    },
    "lower left tiles": {
        "ll1": {
            "connected to": {
                "c1": "east",
                "ll2": "west"
            }
        },
        "ll2": {
            "connected to": {
                "ll1": "east",
                "ll3": "west"
            }
        },
        "ll3": {
            "connected to": {
                "ll2": "east",
                "ll4": "west"
            }
        },
        "ll4": {
            "connected to": {
                "ll3": "east",
                "ll5": "west"
            }
        },
        "ll5": {
            "connected to": {
                "ll4": "east",
                "g4": "west",
                "l1": "north"
            }
        }
    },
    "lower right tiles": {
        "lr1": {
            "connected to": {
                "c1": "west",
                "lr1": "east"
            }
        },
        "lr2": {
            "connected to": {
                "lr1": "west",
                "lr3": "east"
            }
        },
        "lr3": {
            "connected to": {
                "lr2": "west",
                "lr4": "east" 
            }
        },
        "lr4": {
            "connected to": {
                "lr3": "west",
                "lr5": "east"
            }
        },
        "lr5": {
            "connected to": {
                "lr4": "west",
                "g8": "east",
                "r1": "north"
            }
        }
    },
    "left tiles": {
        "l1": {
            "connected to": {
                "ll5": "south",
                "l2": "north"
            }
        },
        "l2": {
            "connected to": {
                "l1": "south",
                "l3": "north"
            }
        },
        "l3": {
            "connected to": {
                "l2": "south",
                "l4": "north"
            }
        },
        "l4": {
            "connected to": {
                "l3": "south",
                "l5": "north"
            }
        },
        "l5": {
            "connected to": {
                "l4": "south",
                "l6": "north"
            }
        },
        "l6": {
            "connected to": {
                "l5": "south",
                "l7": "north",
                "cl1": "east"
            }
        },
        "l7": {
            "connected to": {
                "l6": "south",
                "l8": "north"
            }
        },
        "l8": {
            "connected to": {
                "l7": "south",
                "l9": "north"
            }
        },
        "l9": {
            "connected to": {
                "l8": "south",
                "l10": "north"
            }
        },
        "l10": {
            "connected to": {
                "l9": "south",
                "l11": "north"
            }
        },
        "l11": {
            "connected to": {
                "l10": "south",
                "l12": "north"
            }
        },
        "l12": {
            "connected to": {
                "l11": "south",
                "l13": "north"
            }
        },
        "l13": {
            "connected to": {
                "l12": "south",
                "ul1": "east"
            }
        }
    },
    "right tiles": {
        "r1": {
            "connected to": {
                "lr5": "south",
                "r2": "north"
            }
        },
        "r2": {
            "connected to": {
                "r1": "south",
                "r3": "north"
            }
        },
        "r3": {
            "connected to": {
                "r2": "south",
                "r4": "north"
            }
        },
        "r4": {
            "connected to": {
                "r3": "south",
                "r5": "north"
            }
        },
        "r5": {
            "connected to": {
                "r4": "south",
                "r6": "north"
            }
        },
        "r6": {
            "connected to": {
                "r5": "south",
                "r7": "north",
                "cr1": "west"
            }
        },
        "r7": {
            "connected to": {
                "r6": "south",
                "r8": "north"
            }
        },
        "r8": {
            "connected to": {
                "r7": "south",
                "r9": "north"
            }
        },
        "r9": {
            "connected to": {
                "r8": "south",
                "r10": "north"
            }
        },
        "r10": {
            "connected to": {
                "r9": "south",
                "r11": "north"
            }
        },
        "r11": {
            "connected to": {
                "r10": "south",
                "r12": "north"
            }
        },
        "r12": {
            "connected to": {
                "r11": "south",
                "r13": "north"
            }
        },
        "r13": {
            "connected to": {
                "r12": "south",
                "ur1": "west"
            }
        }
    },
    "upper left tiles": {
        "ul1": {
            "connected to": {
                "l13": "west",
                "ul2": "east"
            }
        },
        "ul2": {
            "connected to": {
                "ul1": "west",
                "ul3": "east"
            }
        },
        "ul3": {
            "connected to": {
                "ul2": "west",
                "ul4": "east"
            }
        },
        "ul4": {
            "connected to": {
                "ul3": "west",
                "c10": "east"
            }
        }
    },
    "upper right tiles": {
        "ur1": {
            "connected to": {
                "r13": "east",
                "ur2": "west"
            }
        },
        "ur2": {
            "connected to": {
                "ur1": "east",
                "ur3": "west"
            }
        },
        "ur3": {
            "connected to": {
                "ur2": "east",
                "ur4": "west"
            }
        },
        "ur4": {
            "connected to": {
                "ur3": "east",
                "c10": "west"
            }
        }
    }
}