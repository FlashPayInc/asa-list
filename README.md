![asa-list](https://user-images.githubusercontent.com/64005663/151940730-7aec2e05-c4f5-42af-ada3-b35c614826fd.png)

# FlashPay - Algorand Standard Assets List

This repository contains a list of assets supported on FlashPay.

## Adding Support for Other ASAs

- First of all, the asset icons should be properly updated for the repository. The following rules must be followed for icons.
    -   The icon must have both **SVG** and **PNG** versions.
    -   Icon sizes should be square, **256x256px** for both SVG and PNG versions. Landscape, portrait icons will not be accepted. *(Icons sent other than 256x256px will not be accepted.)*
    -   Note that these icons will mostly be used in rounded areas. Elements located at the corners of the container may not be visible in some applications.
    -   SVG and PNG files should be consistent. All the elements (colors, size, elements’ position, text elements etc.) should look the same in both versions. **(Grayscale image-traced SVG files will not be accepted.)**
    -   The SVG version must be compatible with web-rendering. These icons will mostly be used in Algorand applications. For example, if the SVG file does not appear in GitHub preview, it means it is not compatible.
    -   The SVG version should mostly not contain images. Your icon should have a vector version. (Again, not grayscale image-traced...)
    -   It would be better if your icons have a background. Icons consisting of pure-black or pure-white elements can cause problems in light mode and dark mode applications.
- Icon file names should be **`icon.png`** and **`icon.svg`**.
    -   File names are **case-sensitive**. Icon.png or ICON.png will not be accepted.
- Icon files should be located inside of a folder in the repository under `assets/` directory. This folder's name should be **`unit_name-asset_id`**, e.g. *"USDC-31566704"* without adding any space.
    -   **Unit names are case sensitive.** Make sure you are typing the exact unit name, paying attention to case sensitivity.
- If you think you paid attention to all these in your commit, create a pull request. Pull requests should be into `main` & `test` branches which represent mainnet and testnet respectively. When your PR is accepted, it will be merged with the main branch along with the other icons. Empty PRs and icons sent by adding comments will not be accepted.

**Make sure that all commits are signed. Learn more about signing commits [here](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits).**

## Credits
- [tinymanorg/asa-list](https://github.com/tinymanorg/asa-list)