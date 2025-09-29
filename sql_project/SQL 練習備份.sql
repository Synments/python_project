-- 1. 建立資料庫 (Schema)
CREATE DATABASE hr_data;

-- 2. 告訴 MySQL 我們要使用這個資料庫
USE hr_data;

-- 3. 建立 'employees' 表格
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE
);

-- 4. 插入測試數據
INSERT INTO employees (employee_id, first_name, last_name, department, salary, hire_date) 
VALUES
(101, 'Alice', 'Chen', 'Sales', 65000.00, '2022-01-15'),
(102, 'Bob', 'Lin', 'HR', 55000.00, '2023-05-20'),
(103, 'Charlie', 'Wang', 'Sales', 72000.00, '2021-08-01'),
(104, 'David', 'Kuo', 'Marketing', 60000.00, '2023-11-10'),
(105, 'Eve', 'Zhan', 'HR', 58000.00, '2024-02-28');

-- 練習 1：查詢 employees 表格中的所有欄位 (*) 
SELECT * 
FROM employees; 

-- 練習 2：僅查詢員工的 名字、姓氏 和 薪水 三個欄位 
SELECT first_name, last_name, salary
FROM employees; 

-- 練習 3：查詢所有薪水大於 60000 的員工 
SELECT * 
FROM employees 
WHERE salary > 60000; 

SELECT * 
FROM employees 
WHERE department = 'HR'; 

SELECT * 
FROM employees 
WHERE department = 'Sales' AND salary > 70000; 

-- 練習 6: 查詢所有屬於 HR 部門 OR 薪水高於 70000 的員工 
SELECT * 
FROM employees 
WHERE department = 'HR' OR salary > 70000;

-- 練習 7：查詢所有員工，並依薪水降序排列 
SELECT * 
FROM employees 
ORDER BY salary DESC; 

SELECT * 
FROM employees 
ORDER BY salary DESC      -- 先按薪水降序排列 
LIMIT 2;                  -- 再取出前 2 筆數據 

-- 練習 9：按部門分組，並計算每個部門的平均薪水 
SELECT 
    department,                  -- 這是分組的欄位 
    AVG(salary) AS avg_salary    -- 計算平均薪水，並將結果命名為 avg_salary 
FROM 
    employees
GROUP BY 
    department;                  -- 必須根據 department 欄位進行分組 

-- 練習 10：按部門分組，計算每個部門的員工總數，並依人數降序排列 
SELECT 
    department,
    COUNT(employee_id) as total_employees     -- 使用 COUNT() 函數計算人數 
FROM 
    employees 
GROUP BY 
    department
ORDER BY 
    total_employees DESC;        -- 依據新欄位 total_employees 進行降序排列

-- 1. 建立 'departments' 表格 
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,           -- 部門 ID 
    dept_name VARCHAR(50) NOT NULL,    -- 部門名稱 
    manager_name VARCHAR(50)           -- 部門經理 
); 

-- 2. 插入測試數據 (注意：R&D 部門沒有員工) 

INSERT INTO departments (dept_id, dept_name, manager_name)
VALUES 
(1, 'Sales', 'Michael'), 
(2, 'HR', 'Jessica'), 
(3, 'Marketing', 'Emily'), 
(4, 'R&D', 'Chris'); 
