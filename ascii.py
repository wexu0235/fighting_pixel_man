# ascii.py

class Ascii:
    def __init__(self):
        self.initial = self.pad_ascii(r'''
        ____
       /    \
       \____/
   0   __||__   0
    \ |      | /
     \|      |/
      \______/
        //\\
       //  \\
      //    \\
     //      \\
''')

        self.normal_attack = self.pad_ascii(r'''
       ____
      /*  *\
      \____/
      __||__  / *
     |      |/\
     |      |
     \______/
       //\\
      //  \\
     //    \\
    //      \\
''')

        self.pc_normal_attack = self.pad_ascii(r'''
         ____
        /*  *\
        \____/
   * \  __||__ 
     /\|      |
       |      |
       \______/
         //\\
        //  \\
       //    \\
      //      \\
''')
      
        self.element_attack = self.pad_ascii(r'''
       ____
      /*  *\
      \____/
      __||__  /e e
     |      |/\
     |      |
     \______/
       //\\
      //  \\
     //    \\
    //      \\
''')

        self.pc_element_attack = self.pad_ascii(r'''
         ____
        /*  *\
        \____/
  e e\  __||__ 
     /\|      |
       |      |
       \______/
         //\\
        //  \\
       //    \\
      //      \\
''')


        self.special_attack = self.pad_ascii(r'''
       ____
      /*  *\
      \____/
      __||__  /ssss
     |      |/\ssss
     |      |  
     \______/
       //\\
      //  \\
     //    \\
    //      \\
''')


        self.pc_special_attack = self.pad_ascii(r'''
         ____
        /*  *\
        \____/
 ssss\  __||__
 ssss/\|      |
       |      |
       \______/
         //\\
        //  \\
       //    \\
      //      \\
''')

        self.defend = self.pad_ascii(r'''
       ____
      /0  0\
      \____/
      __||__
    {|000000|}
    {|000000|}
     \______/
       //\\
      //  \\
     //    \\
    //      \\
''')

        self.pc_defend = self.pad_ascii(r'''
       ____
      /0  0\
      \____/
      __||__
    {|000000|}
    {|000000|}
     \______/
       //\\
      //  \\
     //    \\
    //      \\
''')
       
        self.reflect = self.pad_ascii(r'''
       ____
      /~  ~\
      \____/
      __||__  /~~
     |~~~~~~|/\
     |~~~~~~|
     \______/
       //\\
      //  \\
     //    \\
    //      \\
''')

       
        self.pc_reflect = self.pad_ascii(r'''
       ____
      /~  ~\
      \____/
 ~~\  __||__  
   /\|~~~~~~|
     |~~~~~~|
     \______/
       //\\
      //  \\
     //    \\
    //      \\
''')

        self.fall = self.pad_ascii(r'''
       ____
      /@  @\
      \____/
      __||__
    /|000000|\
   / |  @@  | \
  /  \______/  \
       //\\
  ====//  \\====
''')


        self.win = self.pad_ascii(r'''
       ____
 v    /^  ^\   v
  \   \____/   /
   \  __||__  /
    \|      |/
     |      |
     \______/
       //\\
      //  \\
     //    \\
    //      \\
''')


    def pad_ascii(self, art: str, target_lines: int = 14) -> str:
        lines = art.strip("\n").splitlines()
        lines += [""] * (target_lines - len(lines))
        return "\n".join(lines)

ascii = Ascii()


def print_side_by_side(left: str, right: str, left_name: str = "Player", right_name: str = "PC") -> None:
    left_lines = left.strip("\n").splitlines()
    right_lines = right.strip("\n").splitlines()

    max_lines = max(len(left_lines), len(right_lines))
    left_lines += [""] * (max_lines - len(left_lines))
    right_lines += [""] * (max_lines - len(right_lines))

    print(f"{left_name:<35}{right_name}")
    for l, r in zip(left_lines, right_lines):
        print(f"{l:<35}{r}")

