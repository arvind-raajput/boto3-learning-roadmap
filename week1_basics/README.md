# Week 1 – Python & Boto3 Basics 🚀

Welcome to **Week 1** of the *boto3 learning roadmap*!  
This week focuses on getting comfortable with **Python scripting basics** and making your **first boto3 calls** to AWS.

---

## 🎯 Learning Goals
- Refresh Python scripting basics (variables, loops, functions).
- Set up AWS credentials locally.
- Install and configure boto3.
- Write your first boto3 script: **list all S3 buckets**.

---

## 📚 Study Plan
1. **Python Basics Refresher**
   - Variables, data types, and conditionals
   - Loops (`for`, `while`)
   - Functions (`def`)
   - Importing modules

2. **AWS CLI & Credentials Setup**
   - Install AWS CLI
   - Run `aws configure` to set up credentials
   - Verify with:
     ```bash
     aws s3 ls
     ```

3. **Install boto3**
   ```bash
   pip install boto3
