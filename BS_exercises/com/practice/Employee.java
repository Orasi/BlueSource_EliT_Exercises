package com.practice;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class Employee {

    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\chromedriver_win32\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();

        //Log into BlueSource

        driver.navigate().to("http://bluesourcestaging.herokuapp.com/login");

        WebElement usernameField = driver.findElement(By.id("employee_username"));
        usernameField.sendKeys("company.admin");

        WebElement passwordField = driver.findElement(By.id("employee_password"));
        passwordField.sendKeys("1234");

        WebElement loginBtn = driver.findElement(By.xpath("//*[@id=\"new_employee\"]/div[2]/div[3]/input"));
        loginBtn.submit();

        Thread.sleep(5000);

        //Adding a new employee

        WebElement addBtn = driver.findElement(By.cssSelector("#all-content > div.header-btn-section > div > div.btn-group.pull-right"));
        addBtn.click();

        Thread.sleep(5000);


        WebElement empUsernameField = driver.findElement(By.name("employee[username]"));
        empUsernameField.sendKeys("Bethompson");


        WebElement empFirstnameField = driver.findElement(By.name("employee[first_name]"));
        empFirstnameField.sendKeys("bRIAN");

        WebElement empLastnameField = driver.findElement(By.name("employee[last_name]"));
        empLastnameField.sendKeys("tHOMPSON");


        new Select(driver.findElement(By.name("employee[title_id]"))).selectByVisibleText("wow 1");

        new Select(driver.findElement(By.name("employee[manager_id]"))).selectByVisibleText("Carla Wilson");

        new Select(driver.findElement(By.name("employee[location]"))).selectByVisibleText("Greensboro");

        new Select(driver.findElement(By.name("employee[im_client]"))).selectByVisibleText("AIM");

        WebElement createBtn = driver.findElement(By.name("commit"));
        createBtn.click();

        Thread.sleep(5000);

        driver.quit();

    }

}
