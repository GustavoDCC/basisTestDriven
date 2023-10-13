Feature: Decay Product
    In order to keep fresh products
    As an inventory keeper
    I want to track product quality over time

    Scenario: Discount product quality over time
     Given a product
     When time passes
     Then product quality should deteriorate