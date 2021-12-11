package main

var __author__ = "Liam Thomas-Chollier"
var __copyright__ = "Copyright (C) 2021 Liam Thomas-Chollier"
var __license__ = "Public Domain"
var __version__ = "1.0"

import "random"

var base = []int{2, 10, 16}
var dico = map[int][]int{2: []int{10, 16}, 10: []int{2, 16}, 16: []int{2, 10}}

func init() {
	rand.Seed(time.Now().UnixNano())
}
func binaire(n interface {
}) {
	"{:0b}".format(n)
}
func hexa(n interface {
}) {
	"{:0x}".format(n)
}
func decimal(number interface {
}, base []int) int {
	return int(number, base)
}
func askhex(num interface {
}) bool {
	return hexa(num) == strings.ToLower(fmt.Sprintf("%v", func(msg string) string {
		fmt.Print(msg)
		text, _ := bufio.NewReader(os.Stdin).ReadString('\n')
		return strings.ReplaceAll(text, "\n", "")
	}("Nombre en Hexa :")))
}
func askbin(num interface {
}) bool {
	return binaire(num) == strings.ToLower(fmt.Sprintf("%v", func(msg string) string {
		fmt.Print(msg)
		text, _ := bufio.NewReader(os.Stdin).ReadString('\n')
		return strings.ReplaceAll(text, "\n", "")
	}("Nombre en Binaire :")))
}
func askdec(num interface {
}) bool {
	return reflect.DeepEqual(num, func() int {
		i, err := strconv.ParseInt(func(msg string) string {
			fmt.Print(msg)
			text, _ := bufio.NewReader(os.Stdin).ReadString('\n')
			return strings.ReplaceAll(text, "\n", "")
		}("Nombre en Decimal :"), 10, 64)
		if err != nil {
			panic(err)
		}
		return int(i)
	}())
}
func ask(base []int) {
	if reflect.DeepEqual(base, 2) {
		for !askbin(list[0]) {
			fmt.Println("raté reesayes")
		}
		fmt.Println("Bravo")
	} else if reflect.DeepEqual(base, 10) {
		for !askdec(list[0]) {
			fmt.Println("raté reesayes")
		}
		fmt.Println("Bravo")
	} else if reflect.DeepEqual(base, 16) {
		for !askhex(list[0]) {
			fmt.Println("raté reesayes")
		}
		fmt.Println("Bravo")
	} else {
		fmt.Println("Erreur de Base")
	}
}
func init() {
	for {
		basedep := 0
		list := []interface {
		}{}
		list = append(list, func(start int, stop int) int {
			n := stop - start
			return rand.Intn(n) + start
		}(0, 255+1))
		list = append(list, fmt.Sprintf("%v", binaire(list[0])))
		list = append(list, fmt.Sprintf("%v", hexa(list[0])))
		for func() int {
			for i, v := range base {
				if v == basedep {
					return i
				}
			}
			return -1
		}() == -1 {
			basedep = func() int {
				i, err := strconv.ParseInt(func(msg string) string {
					fmt.Print(msg)
					text, _ := bufio.NewReader(os.Stdin).ReadString('\n')
					return strings.ReplaceAll(text, "\n", "")
				}("Quelle base de depart (2,10,16): "), 10, 64)
				if err != nil {
					panic(err)
				}
				return int(i)
			}()
			if func() int {
				for i, v := range base {
					if v == basedep {
						return i
					}
				}
				return -1
			}() == -1 {
				fmt.Println("Base non prise en charge")
			}
			if basedep == 2 {
				fmt.Println("nombre :", list[1])
				for _, item := range dico[2] {
					ask(item)
				}
			} else if basedep == 10 {
				fmt.Println("nombre :", list[0])
				for _, item := range dico[10] {
					ask(item)
				}
			} else if basedep == 16 {
				fmt.Println("nombre :", list[2])
				for _, item := range dico[16] {
					ask(item)
				}
			} else {
				fmt.Println("erreur")
				os.Exit(2)
			}
		}
		fmt.Println("Bravo vous avez fait : %s -> %s -> %s " % string([3]interface {
		}{list[0], list[1], list[2]}))
	}
}

// <standard input>:8:1: expected declaration, found 'import'
// <standard input>:8:1: expected declaration, found 'import'
// [2021-12-11 23:23:20] FATAL Error formatting source: exit status 2