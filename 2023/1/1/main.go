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

func getCalibrationValues(file *os.File) ([]int, error) {
	totals := make([]int, 0)

	// each word from input
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// numbers := make([]int, 0)
		var firstValue string
		var lastValue string

		s := bufio.NewScanner(strings.NewReader(scanner.Text()))
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
}
