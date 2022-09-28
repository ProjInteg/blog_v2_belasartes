    window.onload = function() {
			var elementBody = document.querySelector('html');
			var elementBtnIncreaseFont = document.getElementById('increase-font');
			var elementBtnDecreaseFont = document.getElementById('decrease-font');
			var fontSize = 100;
			var increaseDecrease = 10;

			elementBtnIncreaseFont.addEventListener('click', function(event) {
				fontSize = fontSize + increaseDecrease;
				elementBody.style.fontSize = fontSize + '%';
			});

			elementBtnDecreaseFont.addEventListener('click', function(event) {
				fontSize = fontSize - increaseDecrease;
				elementBody.style.fontSize = fontSize + '%';
			});
            }
