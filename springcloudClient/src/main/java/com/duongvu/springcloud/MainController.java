package com.duongvu.springcloud;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MainController {
    @Value("${spring.maxAttempts}")
    private String cron;

    @RequestMapping(value = "/getCronformat")
    @ResponseBody
    public String getCronFormat(){
        return  cron;
    }
}
