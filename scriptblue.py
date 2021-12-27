from random import randint,choice


def ActRobot(robot):

        if (robot.investigate_down() == 'enemy-base' or robot.investigate_up() == 'enemy-base' or robot.investigate_right() == 'enemy-base' or robot.investigate_left() == 'enemy-base' or robot.investigate_ne() == 'enemy-base' or robot.investigate_nw() == 'enemy-base' or robot.investigate_se() == 'enemy-base' or robot.investigate_sw() == 'enemy-base'):
                robot.DeployVirus(robot.GetVirus())
                return 0
        
        if (robot.investigate_down() == 'enemy' or robot.investigate_up() == 'enemy' or robot.investigate_right() == 'enemy' or robot.investigate_left() == 'enemy' or robot.investigate_ne() == 'enemy' or robot.investigate_nw() == 'enemy' or robot.investigate_se() == 'enemy' or robot.investigate_sw() == 'enemy'):
                robot.DeployVirus(800)
                if robot.GetYourSignal() != 'stay' and robot.GetYourSignal() != 'patrol':
                        if robot.investigate_up() == 'enemy' or robot.investigate_up() == 'enemy-base':
                                return choice([2, 3, 4])
                        elif robot.investigate_right() == 'enemy' or robot.investigate_right() == 'enemy-base':
                                return choice([1, 3, 4])
                        elif robot.investigate_down() == 'enemy' or robot.investigate_down() == 'enemy-base':
                                return choice([2, 1, 4])
                        elif robot.investigate_left() == 'enemy' or robot.investigate_left() == 'enemy-base':
                                return choice([2, 3, 1])
        
        if robot.GetInitialSignal() == 'patrol':
                
                if (robot.investigate_down() == 'friend-base' or robot.investigate_up() == 'friend-base' or robot.investigate_right() == 'friend-base' or robot.investigate_left() == 'friend-base' or robot.investigate_ne() == 'friend-base' or robot.investigate_nw() == 'friend-base' or robot.investigate_se() == 'friend-base' or robot.investigate_sw() == 'friend-base'):
                        return 0
                elif robot.investigate_up() == 'blank':
                        robot.setSignal('stay')
                        return 1
                elif robot.investigate_right() == 'blank':
                        robot.setSignal('stay')
                        return 2
                elif robot.investigate_down() == 'blank':
                        robot.setSignal('stay')
                        return 3
                elif robot.investigate_left() == 'blank':
                        robot.setSignal('stay')
                        return 4
                else:
                        robot.setSignal('explore')
                        return randint(1,4)

        elif robot.investigate_up() == 'wall':
                return choice([2, 3, 4])
        elif robot.investigate_right() == 'wall':
                return choice([1, 3, 4])
        elif robot.investigate_down() == 'wall':    
                return choice([2, 1, 4])
        elif robot.investigate_left() == 'wall':      
                return choice([2, 3, 1])
        else:
                return randint(1,4)



def ActBase(base):

        if (base.investigate_down() == 'enemy' or base.investigate_up() == 'enemy' or base.investigate_right() == 'enemy' or base.investigate_left() == 'enemy' or base.investigate_ne() == 'enemy' or base.investigate_nw() == 'enemy' or base.investigate_se() == 'enemy' or base.investigate_sw() == 'enemy') or (base.investigate_down() == 'enemy-base' or base.investigate_up() == 'enemy-base' or base.investigate_right() == 'enemy-base' or base.investigate_left() == 'enemy-base' or base.investigate_ne() == 'enemy-base' or base.investigate_nw() == 'enemy-base' or base.investigate_se() == 'enemy-base' or base.investigate_sw() == 'enemy-base'):
                base.DeployVirus(2400)
        if base.GetElixir() > 1800:
                base.create_robot('patrol')
        elif base.GetElixir() > 700:
                base.create_robot('explore')

        return

# this is a test message to check git.