const js = require('@eslint/js');
const tseslint = require('@typescript-eslint/eslint-plugin');
const tsparser = require('@typescript-eslint/parser');
const sveltePlugin = require('eslint-plugin-svelte');
const svelteParser = require('svelte-eslint-parser');
const prettierConfig = require('eslint-config-prettier');

module.exports = [
  // Ignorer les dossiers et fichiers non pertinents
  {
    ignores: [
      'node_modules/**',
      '.venv/**',
      'venv/**',
      'dist/**',
      'build/**',
      '*.config.js',
      '*.config.cjs',
      '*.config.mjs',
      '*.min.js',
      '*.bundle.js',
      '.tmp/**',
      '.temp/**',
    ],
  },

  // Configuration de base pour tous les fichiers
  {
    files: ['**/*.{js,ts,svelte}'],
    languageOptions: {
      ecmaVersion: 2020,
      sourceType: 'module',
      globals: {
        // Variables globales du navigateur
        window: 'readonly',
        document: 'readonly',
        console: 'readonly',
        setTimeout: 'readonly',
        clearTimeout: 'readonly',
        setInterval: 'readonly',
        clearInterval: 'readonly',
        fetch: 'readonly',
        // Variables globales Node.js
        process: 'readonly',
        Buffer: 'readonly',
        __dirname: 'readonly',
        __filename: 'readonly',
        module: 'readonly',
        require: 'readonly',
        exports: 'readonly',
        global: 'readonly',
      },
    },
    plugins: {
      '@typescript-eslint': tseslint,
      svelte: sveltePlugin,
    },
    rules: {
      // Base ESLint rules
      ...js.configs.recommended.rules,
 
      // General rules
      'no-console': 'warn',
      'no-debugger': 'error',
      'prefer-const': 'error',
      'no-var': 'error',
      'no-unused-vars': 'off', // Disabled because we use the TypeScript version
    },
  },

  // Specific configuration for TypeScript files
  {
    files: ['**/*.ts'],
    languageOptions: {
      parser: tsparser,
      parserOptions: {
        ecmaVersion: 2020,
        sourceType: 'module',
      },
    },
    rules: {
      ...tseslint.configs.recommended.rules,
 
      // Custom TypeScript rules
      '@typescript-eslint/no-unused-vars': [
        'error',
        { argsIgnorePattern: '^_' },
      ],
      '@typescript-eslint/no-explicit-any': 'warn',
      '@typescript-eslint/explicit-function-return-type': 'off',
      '@typescript-eslint/explicit-module-boundary-types': 'off',
      '@typescript-eslint/no-non-null-assertion': 'warn',
    },
  },

  // Specific configuration for Svelte files
  {
    files: ['**/*.svelte'],
    languageOptions: {
      parser: svelteParser,
      parserOptions: {
        parser: tsparser,
        ecmaVersion: 2020,
        sourceType: 'module',
      },
    },
    rules: {
      ...sveltePlugin.configs.recommended.rules,
 
      // Custom Svelte rules
      'svelte/no-at-html-tags': 'error',
      'svelte/no-target-blank': 'error',
      'svelte/valid-compile': 'error',
      'svelte/no-reactive-functions': 'error',
      'svelte/no-reactive-literals': 'error',
      'svelte/no-useless-mustaches': 'error',
      'svelte/prefer-class-directive': 'error',
      'svelte/prefer-style-directive': 'error',
      'svelte/shorthand-attribute': 'error',
      'svelte/shorthand-directive': 'error',
    },
    settings: {
      'svelte/typescript': true,
    },
  },

  // Prettier configuration (must be last to disable conflicting rules)
  prettierConfig,
];
