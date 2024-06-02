function printSquare(size) {
  // Loop through each row
  for (let i = 0; i < size; i++) {
    // Print a line of hashtags for each row
    let row = "";
    for (let j = 0; j < size; j++) {
      row += "#";
    }
    console.log(row); // Print the entire row after building it
  }
}

// Example usage with size 10
printSquare(10);
