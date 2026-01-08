#صورت سؤال# پروژه: سیستم مدیریت انبار (Inventory System)
#یک برنامه پایتون بنویسید که یک سیستم مدیریت انبار ساده را پیاده‌سازی کند. برنامه باید به کاربر یک منو نمایش دهد و اجازه دهد عملیات زیر را انجام دهد:
#:heavy_check_mark: عملیات مورد نیاز:
#افزودن محصول جدید
#دریافت نام محصول
#دریافت قیمت محصول
#دریافت تعداد موجودی
#ذخیره اطلاعات در لیست
#حذف محصول
#دریافت نام محصول
#حذف محصول اگر وجود داشت
#نمایش پیام خطا اگر وجود نداشت
#ویرایش محصول
#انتخاب اینکه قیمت تغییر کند یا موجودی
#تغییر مقدار جدید
#نمایش همه محصولات
# ن#مایش نام، قیمت و موجودی همه محصولات
#جستجوی محصول
#دریافت نام
#مایش اطلاعات محصول در صورت یافت شدن
#محاسبه ارزش کل انبار
#حاسبه مجموع (قیمت × تعداد موجودی) برای همه محصولات
#خرید محصول
#دریافت نام محصول#
#کاهش موجودی پس از خرید#
#پیام خطا در صورت نبودن محصول یا موجودی ناکافی#
#خروج از برنامه
#برنامه باید تا زمانی که کاربر گزینه خروج را انتخاب نکرده، به اجرای خود ادامه دهد.
#:us: Project Description (English Version)#
# Project Task: Inventory Management System
#Write a Python program that implements a simple Inventory Management System. The program should display a menu and allow the user to perform the following operations:
#:heavy_check_mark: Required Features:
#Add New Product
#Input product name
#Input product price
#Input stock quantity
#Store data in a list
#Remove Product
#Input product name
#Remove if it exists
#Show an error message if not found
#Edit Product
#Choose to update price or stock
#Save the new value
#Show All Products
#Display name, price, and stock of every product
#Search Product
#Input product name
#Display details if product exists
#Calculate Total Inventory Value
#Compute: price × stock for each product
#Sum all values
#Buy Product
#Input product name
#Reduce stock automatically
#Error if product not found or stock insufficient
#Exit Program
#The program should continue running until the user selects the exit option.



products = []

while True:
    print("\n--- Store Management System ---")
    print("1. Add product")
    print("2. Remove product")
    print("3. Edit product")
    print("4. Show all products")
    print("5. Search product")
    print("6. Buy product")
    print("7. Total inventory value")
    print("8. Exit")

    choice = input("Choose an option (1-8): ")

    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        products.append([name, price, stock])
        print("Product added successfully.")

    elif choice == "2":
        remove_name = input("Enter product name to remove: ")
        found = False

        for product in products:
            if product[0] == remove_name:
                products.remove(product)
                found = True
                print("Product removed successfully.")
                break

        if not found:
            print("Product not found.")

    elif choice == "3":
        edit_name = input("Enter product name to edit: ")
        found = False

        for product in products:
            if product[0] == edit_name:
                found = True
                print("What do you want to edit?")
                print("1. Price")
                print("2. Stock")
                edit_choice = input("Choose: ")

                if edit_choice == "1":
                    new_price = float(input("Enter new price: "))
                    product[1] = new_price
                    print("Price updated.")

                elif edit_choice == "2":
                    new_stock = int(input("Enter new stock quantity: "))
                    product[2] = new_stock
                    print("Stock updated.")

                else:
                    print("Invalid option.")

                break

        if not found:
            print("Product not found.")

    elif choice == "4":
        if len(products) == 0:
            print("No products available.")
        else:
            for product in products:
                print("Name:", product[0], "- Price:", product[1], "- Stock:", product[2])

    elif choice == "5":
        search_name = input("Enter product name to search: ")
        found = False

        for product in products:
            if product[0] == search_name:
                found = True
                print("Product found:")
                print("Name:", product[0], "- Price:", product[1], "- Stock:", product[2])
                break

        if not found:
            print("Product not found.")

    elif choice == "6":
        buy_name = input("Enter product name to buy: ")
        found = False

        for product in products:
            if product[0] == buy_name:
                found = True
                quantity = int(input("How many do you want to buy? "))

                if quantity <= product[2]:
                    total_price = quantity * product[1]
                    product[2] -= quantity
                    print("Purchase successful! Total price:", total_price)
                else:
                    print("Not enough stock available.")
                break

        if not found:
            print("Product not found.")

    elif choice == "7":
        total_value = 0
        for product in products:
            total_value += product[1] * product[2]
        print("Total inventory value:", total_value)

    elif choice == "8":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")

                    
      
        
                    

                    
                    






