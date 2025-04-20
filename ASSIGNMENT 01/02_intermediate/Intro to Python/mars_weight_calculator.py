def main():
    print("🚀 Welcome to the Planetary Weight Calculator 🌍🌌")
    earth_weight = float(input("🌍 Enter your weight on Earth: "))
    planet = input("🪐 Enter a planet (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ")

    # Dictionary with gravity conversion factors
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    if planet in gravity_factors:
        planet_weight = round(earth_weight * gravity_factors[planet], 2)
        print(f"\n✨ The equivalent weight on {planet}: {planet_weight} kg 🪐")
    else:
        print("❌ Invalid planet name. Please try again with a valid planet.")


# Required to run main
if __name__ == "__main__":
    main()
