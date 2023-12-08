package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"unicode"
	"unicode/utf8"

	"github.com/spatialcurrent/go-math/pkg/math"
)

var digitsMap = map[string]string{
	// replace the second letter of each digit
	// 7fiveonedzbmblrtqfoneightkc
	// becomes
	// 7f5eo1edzbmblrtqfo18kc
	"one":   "o1e",
	"two":   "t2o",
	"three": "t3e",
	"four":  "f4r",
	"five":  "f5e",
	"six":   "s6x",
	"seven": "s7n",
	"eight": "e8t",
	"nine":  "n9e",
}

func getCalibrationValues(file *os.File) ([]int, error) {
	totals := make([]int, 0)

	// each word from input
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// numbers := make([]int, 0)
		var firstValue string
		var lastValue string

		translatedText := scanner.Text()
		for key, value := range digitsMap {
			translatedText = strings.Replace(translatedText, key, value, -1)
		}

		s := bufio.NewScanner(strings.NewReader(translatedText))
		s.Split(bufio.ScanRunes)

		// each character of word
		for s.Scan() {
			b, _ := utf8.DecodeRune(s.Bytes())

			if unicode.IsNumber(b) && firstValue == "" {
				firstValue = s.Text()
				lastValue = s.Text()
			} else if unicode.IsNumber(b) {
				lastValue = s.Text()
			}
		}

		if err := s.Err(); err != nil {
			return nil, err
		}

		i, err := strconv.Atoi(firstValue + lastValue)
		if err != nil {
			return nil, err
		}

		totals = append(totals, i)
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return totals, nil
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	totals, err := getCalibrationValues(file)
	total, _ := math.Sum(totals)
	fmt.Println(total)

	if total != 55652 {
		panic("broke it")
	}
}
