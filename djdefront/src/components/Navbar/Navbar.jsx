import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import IconButton from "@material-ui/core/IconButton";

const styles = (theme) => ({
  root: {
    color: theme.palette.common.white,
  },
});

function Navbar(props) {
  return (
    <AppBar position="static">
      <Toolbar>
        <IconButton
          edge="start"
          /*  className={classes.menuButton} */
          color="inherit"
          aria-label="menu"
        >
          {/*  <MenuIcon /> */}
        </IconButton>
        <Typography
          variant="h6"
          /* className={classes.title} */
        >
          News
        </Typography>
        <Button color="inherit">Login</Button>
      </Toolbar>
    </AppBar>
  );

  /*  <MuiAppBar elevation={0} position="static" {...props} />; */
}

Navbar.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Navbar);
