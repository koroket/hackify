# HackMIT Hackify Picture

## Usage

* http://masakazubando.com/hackify/
* use above link, its currently the oly reigetered domain for fb 

* From Edwin
	* Use Soft Light blending to blend #362487 onto an image. Loop over the image data using the formula found here: https://en.wikipedia.org/wiki/Blend_modes#Soft_Light, or use http://blogs.adobe.com/webplatform/2013/01/28/blending-features-in-canvas/

	* Overlay the transparent .png image attached, again using a loop to apply the overlay formula (https://en.wikipedia.org/wiki/Blend_modes#Overlay)

	* Things to note: image data when loaded into a canvas contains three channels (RGB) and an alpha channel. Make sure that images when loaded are resized to the correct size. The overlay provided is 950px x 950px. Feel free to resize to what you need. 500px x 500px should be okay.