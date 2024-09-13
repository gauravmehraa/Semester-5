package com.example.restservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class RestServiceApplication {
	public static void main(String[] args) {
		SpringApplication.run(RestServiceApplication.class, args);
	}
}

/*
https://spring.io/guides/gs/rest-service#initial
./gradlew build
java -jar .\build\libs\rest-service-0.0.1-SNAPSHOT.jar
*/