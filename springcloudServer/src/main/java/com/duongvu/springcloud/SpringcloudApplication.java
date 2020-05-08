package com.duongvu.springcloud;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.config.server.EnableConfigServer;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@EnableConfigServer
@SpringBootApplication
public class SpringcloudApplication {
	@Value("${spring.cron.format")
	private String cron;

	@GetMapping("/getcron")
	public String getCron()
	{
		return cron;
	}

	public static void main(String[] args) {
		SpringApplication.run(SpringcloudApplication.class, args);
	}

}
