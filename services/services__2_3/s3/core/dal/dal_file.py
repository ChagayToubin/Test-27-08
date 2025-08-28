class DAL:

    @staticmethod
    def load_file(fetch = "../../data/blacklist/weapon_list.txt"):
        with open(fetch, "r", encoding="utf-8") as f:
            return f.read()
