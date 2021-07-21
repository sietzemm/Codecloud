<!DOCTYPE html>
		<?php
				if(isset($_POST['submit'])) 
				{ 
					firstname : echo $_POST["firstname"];
					lastname : echo $_POST["lastname"];
					password : echo $_POST["password"];
					country : echo $_POST["country"];
					comment : echo $_POST["comment"];
       
				}
			?>
<html>
	<head>
		<title>PHP test page</title>
		<link rel="stylesheet" type="text/css" href="layout.css">

		<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">
	</head>

<body>
	<header>
		<h2>PHP Exercises XSS test page </h2>	
		<h5>SIETZE MIN - 346406 - ITV1A - HANZEHOGESCHOOL GRONINGEN, 2016</h5>
	</header>

	 <div class="content-holder">
		<div>Hello user. Enter values</div><br/>
	
			<form name="form1" method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>" >
				<label>First Name : </label>
				<input type="text" name="firstname" ><br/>
				<label>Last Name : </label>
				<input type="text" name="lastname">
				<label>Password : </label>
				<input type="password" name="password">
				
				<label for="country">Country</label>
				<select id="country" name="country">
					<option value="australia">Australia</option>
					<option value="canada">Canada</option>
					<option value="usa">United States</option>
				</select>
				<textarea name="comment" rows="5" cols="40"></textarea>
			
				<input type="submit" name="submit" value="Submit Form">
	    	</form>
		
		<!-- 
			<form action="action2.php" method="get">
				<label>First Name : </label>
				<input type="text" name="firstname" ><br/>
				<label>Last Name : </label>
				<input type="text" name="lastname">
			-->
			<!--	<label for="country">Country</label>
				<select id="country" name="country">
					<option value="australia">Australia</option>
					<option value="canada">Canada</option>
					<option value="usa">USA</option>
				</select>
			--><!-- 
				<input type="submit" value="Send">
	    	</form>
			-->
		</div>

<footer>
	<p> footer hoi tekst</p>
</footer>

<body>

</html>