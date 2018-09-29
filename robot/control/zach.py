import wpilib
from wpilib.interfaces.generichid import GenericHID


import components


class Zach:
    """
        Implements gamepad control via a xbox style gamepad
        
        Currently Gamepad and Zach control modes are the same
    """

    gamepad: wpilib.XboxController
    gamepad_alt: wpilib.XboxController

    drive: components.drive.Drive
    lift: components.lift.Lift
    intake: components.intake.Intake
    grabber: components.grabber.Grabber

    def process(self):
        forward_speed = self.gamepad.getTriggerAxis(GenericHID.Hand.kRight)
        reverse_speed = -self.gamepad.getTriggerAxis(GenericHID.Hand.kLeft)
        total_speed = forward_speed + reverse_speed
        if self.lift.lift_encoder.get() > 700:
            total_speed *= 0.8
        if self.lift.get_setpoint() > 1500:
            total_speed *= 0.8

        self.drive.drive(total_speed, -self.gamepad.getX(GenericHID.Hand.kLeft) * .75)

        self.intake.set_speed(-self.gamepad_alt.getY(GenericHID.Hand.kRight))

        if self.gamepad_alt.getRawButton(6):
            self.grabber.grab()
        elif self.gamepad_alt.getRawButton(5):
            self.grabber.release()

        # if self.gamepad_alt.getAButton():
        #     self.lift.set_setpoint(0)
        # elif self.gamepad_alt.getXButton():
        #     self.lift.set_setpoint(30)
        # elif self.gamepad_alt.getYButton():
        #     self.lift.set_setpoint(80)
        # elif self.gamepad_alt.getBButton():
        #     self.lift.set_setpoint(105)
        if self.gamepad_alt.getAButton():
            self.lift.set_setpoint(0)
        elif self.gamepad_alt.getXButton():
            self.lift.set_setpoint(600)
        elif self.gamepad_alt.getYButton():
            self.lift.set_setpoint(1450)
        elif self.gamepad_alt.getBButton():
            self.lift.set_setpoint(1450)

    def execute(self):
        pass

