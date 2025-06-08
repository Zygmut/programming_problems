package main

import (
	"reflect"
	"testing"
)

type TestCase struct {
	n        int
	expected []int
}

var tests = []TestCase{
	{13, []int{1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9}},
	{2, []int{1, 2}},
}

func TestLexicalOrder(t *testing.T) {
	for idx, test := range tests {
		res := lexicalOrder(test.n)
		if !reflect.DeepEqual(res, test.expected) {
			t.Errorf("Failed Test %d\nGot      %v\nExpected %v\n\n", idx, res, test.expected)
		}
	}
}

func TestLexicalOrderStack(t *testing.T) {
	for idx, test := range tests {
		res := lexicalOrderStack(test.n)
		if !reflect.DeepEqual(res, test.expected) {
			t.Errorf("Failed Test %d\nGot      %v\nExpected %v\n\n", idx, res, test.expected)
		}
	}
}

func TestLexicalOrderStackPreAlloc(t *testing.T) {
	for idx, test := range tests {
		res := lexicalOrderStackPreAlloc(test.n)
		if !reflect.DeepEqual(res, test.expected) {
			t.Errorf("Failed Test %d\nGot      %v\nExpected %v\n\n", idx, res, test.expected)
		}
	}
}

func TestLexicalOrderDynStackPreAlloc(t *testing.T) {
	for idx, test := range tests {
		res := lexicalOrderDynStackPreAlloc(test.n)
		if !reflect.DeepEqual(res, test.expected) {
			t.Errorf("Failed Test %d\nGot      %v\nExpected %v\n\n", idx, res, test.expected)
		}
	}
}
