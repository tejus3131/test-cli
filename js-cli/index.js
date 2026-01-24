#!/usr/bin/env node

import chalk from "chalk";

// Read command line arguments
const args = process.argv.slice(2);

console.log(chalk.blue.bold("\n🚀 Simple JS CLI Test\n"));

if (args.length === 0) {
  console.log(chalk.yellow("No arguments provided."));
} else {
  console.log(chalk.green("You passed these arguments:\n"));

  args.forEach((arg, index) => {
    console.log(chalk.cyan(`${index + 1}. ${arg}`));
  });
}

console.log(chalk.gray("\nCLI finished.\n"));
