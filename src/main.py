import httpx

response = httpx.get("https://example.com")

print(response.status_code)
print(response.text)


def main():
    return 8


if __name__ == "__main__":
    main()
