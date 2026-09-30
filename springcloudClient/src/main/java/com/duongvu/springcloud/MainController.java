package com.duongvu.springcloud;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RefreshScope
@RestController
public class MainController {

    @Value("${spring.maxAttempts:3}")
    private int maxAttempts;

    @GetMapping({"/getCronformat", "/config/max-attempts"})
    public int getMaxAttempts() {
        return maxAttempts;
    }
}
