from flask import Flask, jsonify, request

app = Flask(__name__)

# Example book database with real book titles (You can replace this with a real database)
books = {
    1: {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'available': True},
    2: {'title': '1984', 'author': 'George Orwell', 'available': True},
    3: {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'available': True}
}

@app.route('/checkout', methods=['POST'])
def checkout_book():
    book_id = request.json.get('book_id')
    if book_id and book_id in books:
        if books[book_id]['available']:
            books[book_id]['available'] = False
            book_details = {
                'title': books[book_id]['title'],
                'author': books[book_id]['author']
            }
            return jsonify({'message': f'Book {book_id} checked out successfully', 'book_details': book_details}), 200
        else:
            return jsonify({'message': 'Book is not available'}), 400
    return jsonify({'message': 'Invalid book ID'}), 400

@app.route('/checkin', methods=['POST'])
def checkin_book():
    book_id = request.json.get('book_id')
    if book_id and book_id in books:
        if not books[book_id]['available']:
            books[book_id]['available'] = True
            return jsonify({'message': f'Book {book_id} checked in successfully'}), 200
        else:
            return jsonify({'message': 'Book is already available'}), 400
    return jsonify({'message': 'Invalid book ID'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
