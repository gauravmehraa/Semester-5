package com.example.restservice;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CalculatorController {

	@PostMapping("/calculate")
	public Calculator calculator(@RequestBody CalculatorRequest request) {
		double num1 = request.getNum1();
		double num2 = request.getNum2();
		char operator = request.getOperator().charAt(0);
		double result = 0;
		switch(operator){
			case '+': result = num1 + num2; break;
			case '-': result = num1 - num2; break;
			case '*': result = num1 * num2; break;
			case '/': result = num1 / num2; break;
			default: result = 0;
		}
		return new Calculator(result);
	}
}