from .products import Product

def main():
    main_prompt = "Welcome the Local Inventory Management store\n"
    main_prompt += "1 - Add new product to Inventory\n"
    main_prompt += "2 - View all Products in Inventory\n"
    main_prompt += "3 - Update a Product in Inventory(name, category, price)\n"
    main_prompt += "4 - Delete a Product from inventory\n"
    main_prompt += "5 - Generate Product alert based on stock level\n"
    main_prompt += "6 - Search for a Product in Inventory (name or category)\n"
    main_prompt += "7 - Sort Products in Inventory (price or stock quantity)\n"
    main_prompt += "8 - Enter (exit or q) to close application\n\n"
    main_prompt += "Select an action to perform: "

    isAppStart = False

    while not isAppStart:
        program_inuput = input(main_prompt)

        if program_inuput == 'exit' or '8' or 'q' or 'Q':
            isAppStart = True
        
        if program_inuput == '1':
            product_cat = input("Enter product category: ")
            user_category = Product.category_add(product_cat)
            print(f"Category added to database: {user_category}")
            

            








if __name__ == "__main__":
    main()