package com.practice;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;


public class Title {


    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "C:\\chromedriver_win32\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();

        driver.navigate().to("http://bluesourcestaging.herokuapp.com/login");

       WebElement usernameField = driver.findElement(By.id("employee_username"));
       usernameField.sendKeys("company.admin");

       WebElement passwordField = driver.findElement(By.id("employee_password"));
       passwordField.sendKeys("1234");

       WebElement loginBtn = driver.findElement(By.xpath("//*[@id=\"new_employee\"]/div[2]/div[3]/input"));
       loginBtn.submit();

       WebElement dropDown = driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[1]"));
       dropDown.click();

       WebElement dropDownTitles = driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[1]/ul/li/a[2]"));
       dropDownTitles.click();

       WebElement addTitleBtn = driver.findElement(By.cssSelector("#content > a"));
       addTitleBtn.click();

       WebElement titleTextField = driver.findElement(By.id("title_name"));
       titleTextField.sendKeys("Java auto Test");

       WebElement createTitleBtn = driver.findElement(By.name("commit"));
       createTitleBtn.click();

       driver.quit();

    }
}

