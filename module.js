// module.js

// Export a single function
function sayHello(name) {
  return `Hello, ${name}! Welcome to Node.js modules.`;
}

// Export multiple things
const PI = 3.14159;

function add(a, b) {
  return a + b;
}

// Exporting them all together
module.exports = {
  sayHello,
  add,
  PI
};

